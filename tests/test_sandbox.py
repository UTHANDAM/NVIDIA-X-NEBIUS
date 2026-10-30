import pytest
from backend.sandbox_runner import sandbox_runner

def test_sandbox_passing_code():
    code = """
def add(a, b):
    return a + b
"""
    test = """
from solution import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
"""
    res = sandbox_runner.execute_test(code, test)
    assert res["status"] == "PASSED"
    assert res["exit_code"] == 0

def test_sandbox_failing_code():
    code = """
def add(a, b):
    return a - b  # Bug intentionally introduced
"""
    test = """
from solution import add

def test_add():
    assert add(2, 3) == 5
"""
    res = sandbox_runner.execute_test(code, test)
    assert res["status"] == "FAILED"
    assert res["exit_code"] == 1
    assert "assert add(2, 3) == 5" in res["failure_trace"] or "assert -1 == 5" in res["failure_trace"]
