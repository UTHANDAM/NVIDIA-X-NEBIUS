"""
Sandboxed Execution & Test Runner for NemotronForge.
Executes code and companion test suites in an isolated temporary directory,
capturing stdout, stderr, execution status, and precise failure traces.
Powers the autonomous self-healing feedback loop.
"""
import os
import sys
import uuid
import shutil
import subprocess
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SandboxRunner:
    def __init__(self, base_dir: str = "sandbox_runs"):
        self.base_dir = os.path.abspath(base_dir)
        os.makedirs(self.base_dir, exist_ok=True)

    def execute_test(
        self,
        code_content: str,
        test_content: str,
        timeout_seconds: int = 15
    ) -> Dict[str, Any]:
        """
        Writes code and test files to an isolated subfolder and runs pytest.
        Returns execution telemetry, status, and failure traces.
        """
        run_id = f"run_{uuid.uuid4().hex[:8]}"
        run_path = os.path.join(self.base_dir, run_id)
        os.makedirs(run_path, exist_ok=True)

        solution_file = os.path.join(run_path, "solution.py")
        test_file = os.path.join(run_path, "test_solution.py")

        try:
            with open(solution_file, "w", encoding="utf-8") as f:
                f.write(code_content)
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(test_content)

            # Build command using the current Python executable with isolated cache and minimal overhead
            cmd = [
                sys.executable,
                "-m",
                "pytest",
                "test_solution.py",
                "-v",
                "--tb=short",
                "-p",
                "no:langsmith",
                "-p",
                "no:cov",
                "-o",
                "cache_dir=.run_cache"
            ]

            env = os.environ.copy()
            # Disable external plugin autoloading to ensure ultra-fast sandbox test execution (<1.5s)
            env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
            # Ensure the current directory in python path so tests can import solution
            env["PYTHONPATH"] = f"{run_path}{os.pathsep}{env.get('PYTHONPATH', '')}"

            result = subprocess.run(
                cmd,
                cwd=run_path,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                env=env
            )

            stdout = result.stdout or ""
            stderr = result.stderr or ""
            exit_code = result.returncode
            success = (exit_code == 0)

            # Analyze failures for self-healing feedback
            failure_trace = ""
            if not success:
                failure_trace = self._extract_failure_summary(stdout, stderr)

            return {
                "run_id": run_id,
                "status": "PASSED" if success else "FAILED",
                "exit_code": exit_code,
                "stdout": stdout,
                "stderr": stderr,
                "failure_trace": failure_trace,
                "code_chars": len(code_content),
                "test_chars": len(test_content)
            }

        except subprocess.TimeoutExpired:
            return {
                "run_id": run_id,
                "status": "TIMEOUT",
                "exit_code": -1,
                "stdout": "",
                "stderr": f"Execution timed out after {timeout_seconds} seconds (possible infinite loop).",
                "failure_trace": f"TimeoutExpired: Process exceeded {timeout_seconds}s limit.",
                "code_chars": len(code_content),
                "test_chars": len(test_content)
            }
        except Exception as e:
            logger.error(f"Sandbox runner error: {e}")
            return {
                "run_id": run_id,
                "status": "ERROR",
                "exit_code": -1,
                "stdout": "",
                "stderr": str(e),
                "failure_trace": str(e),
                "code_chars": len(code_content),
                "test_chars": len(test_content)
            }
        finally:
            # Clean up run directory if desired, or retain last few for debugging
            pass

    def _extract_failure_summary(self, stdout: str, stderr: str) -> str:
        """
        Parses pytest short traceback and failure headers to provide focused context for Nemotron.
        """
        lines = stdout.splitlines()
        failures = []
        capture = False

        for line in lines:
            if "FAILURES" in line or "ERRORS" in line:
                capture = True
            if capture:
                failures.append(line)
            if "short test summary info" in line:
                failures.append(line)

        if not failures:
            return stdout[-800:] if len(stdout) > 800 else stdout + "\n" + stderr
        
        return "\n".join(failures[:40])

sandbox_runner = SandboxRunner()
