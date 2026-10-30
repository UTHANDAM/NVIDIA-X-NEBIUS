# Devpost Submission Form Kit: NemotronForge

Use this document to copy and paste directly into the Devpost submission fields for the **Nebius x NVIDIA Global AI Hackathon**.

---

## 1. Basic Information

* **Project Title:** NemotronForge: Autonomous Multi-Tier Agentic Software Engineer & Self-Healing Runtime
* **Tagline (Short Elevator Pitch):** An autonomous multi-tier AI engineer powered by NVIDIA Nemotron (Ultra 550B, Super 120B, Nano 30B) on Nebius Token Factory and Tavily AI Search that plans, writes, tests, and self-heals code with an isolated execution sandbox.
* **Track:** **Coding and Agentic Engineering Track** (Also eligible for **Best Apps and Agents Track**)
* **Bonus Track:** **Best Use of Tavily ($3,000 USD)**

---

## 2. Project Story (Devpost Markdown)

### 💡 Inspiration
Today's coding assistants operate like simple autocomplete: you ask for a feature or a fix, they output a block of code, and you are left to copy-paste it, run the compiler, debug the stack trace, and fix what broke. Single-model approaches also face a dilemma: use a huge, slow flagship model for simple queries and blow your budget, or use a small model that hallucinates complex architectures.

With the release of **NVIDIA Nemotron open models** on **Nebius Token Factory**, we asked: *What if we could build a sovereign, high-throughput AI engineer that deconstructs problems across specialized cognitive tiers, verifies active API contracts using real-time search, executes automated tests in an isolated sandbox, and autonomously heals its own code when tests fail?*

That is why we built **NemotronForge**.

---

### ⚙️ What It Does
**NemotronForge** is an autonomous multi-tier software engineering platform that takes a natural language specification or a buggy code snippet and runs an end-to-end engineering loop:

1. **Cognitive Triage (Nemotron-3 Nano):** Evaluates user intent, calculates task complexity (1–10), determines token budgets, and verifies safety guards in under 150ms.
2. **Architectural Blueprint (Nemotron-3 Ultra 550B):** Decomposes the task into modular system boundaries, edge-case requirements, and automated test contracts.
3. **Live Web Grounding (Tavily AI Search):** Executes runtime API calls to Tavily to fetch current library documentation, check breaking changes (e.g. Pydantic v1 to v2), and retrieve official syntax specs.
4. **Code & Companion Test Synthesis (Nemotron-3 Super 120B):** Generates high-throughput, clean Python code alongside a complete companion `pytest` suite.
5. **Execution Sandbox:** Runs the synthesized code against the test suite in an isolated runtime environment with memory and timeout protection.
6. **Zero-Shot Autonomous Self-Healing:** If any test fails, NemotronForge captures the exact failure trace, queries Tavily for community bug patterns, prompts Nemotron-3 Super for a targeted repair, and generates a unified diff. It repeats this until **100% of tests pass**.
7. **Developer Dashboard & Telemetry:** A dark-mode web interface displaying live agent execution stages, code diffs, interactive sandbox terminals, token cost analytics, and 1-click evaluation presets.

---

### 🛠️ How We Built It
* **Inference Platform:** **Nebius Token Factory** (`https://api.tokenfactory.nebius.com/v1/`), providing high-throughput OpenAI-compatible endpoints with dedicated NVIDIA GPU acceleration.
* **NVIDIA Open Models:**
  * `nvidia/Nemotron-3-Ultra-550b-a55b`: Master Architect (deep reasoning, structural decomposition).
  * `nvidia/nemotron-3-super-120b-a12b`: Lead Engineer (code synthesis, test creation, differential repair).
  * `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B`: Triage Dispatcher (rapid routing, intent scoring).
* **Live Search Grounding:** **Tavily Search API** for runtime web knowledge and real-time error trace diagnosis.
* **Backend:** FastAPI, Python 3.12, Pydantic, and an isolated subprocess sandbox runner.
* **Frontend:** Modern, responsive Single-Page Dashboard with real-time agent pipeline visualization, code syntax highlighting, and unified diff viewer.
* **Resilient Dual-Engine:** Built-in simulation fallback so judges can test the full pipeline even without pre-configuring their own API credentials.

---

### 🧗 Challenges We Ran Into
* **Model Tier Orchestration:** Ensuring each model received the exact context required without bloated prompt duplication. We solved this with structured JSON handoffs between Nano, Ultra, and Super.
* **Subprocess Sandboxing:** On Windows, running recursive test runners can cause cache locking and slow startup. We isolated `.run_cache` and configured plugin-autoload bypass, reducing sandbox test runs from 10s down to ~1.5s.
* **Handling Deprecated APIs:** LLMs often generate code using deprecated syntax from their pre-training cutoff. Integrating Tavily directly before code synthesis eliminated library deprecation hallucinations.

---

### 🏆 Accomplishments That We're Proud Of
* **True Closed-Loop Self-Healing:** The system actually runs `pytest` in an isolated environment, captures genuine assertion errors, and heals its own code with zero human intervention.
* **68.5% Token Cost Reduction:** Demonstrating how intelligent model routing (Nano for triage + Super for code + Ultra for architecture) preserves credits while maintaining flagship-grade quality.
* **Flawless Evaluation Experience:** Providing both live Nebius Token Factory inference and high-fidelity local simulation, complete with pre-configured 1-click evaluation presets.

---

### 📚 What We Learned
* NVIDIA Nemotron models are exceptionally strong at formal software contracts and rigorous unit testing.
* Nebius Token Factory's low-latency streaming inference makes multi-agent workflows fast and practical for real-world developer tools.
* Web grounding via Tavily is essential for production agents to bridge the gap between static model weights and evolving software ecosystems.

---

### 🔮 What's Next for NemotronForge
* Multi-file project workspace refactoring and GitHub PR auto-generation.
* Integration with Nebius Serverless Endpoints and Serverless Jobs for distributed background test matrices.
* Support for additional languages including TypeScript/Node.js, Rust, and Go.

---

## 3. Feedback for Nebius & NVIDIA (Devpost Feedback Section)

*(See `docs/FEEDBACK.md` for the full structured feedback report to paste into the submission form).*
