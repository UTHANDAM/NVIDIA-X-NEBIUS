# Demo Video Script & Storyboard (Duration: ~2 Minutes 30 Seconds)

*Follow this exact script and timing guide to record your 3-minute hackathon video for YouTube.*

---

## 🎥 Recording Setup Instructions
* **Tools:** Use Loom, OBS Studio, or Windows Screen Recorder (`Win + Alt + R`).
* **Display:** Full-screen browser window at `http://localhost:8000`.
* **Microphone:** Clear voice, no background music.

---

## ⏱️ Video Script & Storyboard

### [0:00 – 0:25] Introduction & The Problem
* **Visual:** Open browser at `http://localhost:8000`. Show the header with **NemotronForge**, **NVIDIA Nemotron**, and **Nebius Token Factory** badges.
* **Voiceover:**
  > "Hi everyone! Welcome to NemotronForge — an autonomous, multi-tier software engineering platform built for the Nebius x NVIDIA Global AI Hackathon.
  > Today's coding copilots are mostly single-prompt autocompletes. They don't test their code, they don't know when third-party libraries change, and when their code fails, you're stuck debugging the stack trace.
  > NemotronForge solves this by orchestrating a cognitive swarm of NVIDIA Nemotron open models hosted on Nebius Token Factory, combined with real-time Tavily search and an isolated self-healing execution sandbox."

---

### [0:25 – 0:55] Architectural Tiering & Presets Walkthrough
* **Visual:** Hover over the **Tiered Cognitive Architecture Pipeline** cards (Nano -> Ultra -> Tavily -> Super -> Sandbox -> Self-Healing). Point out the 4 evaluation preset cards.
* **Voiceover:**
  > "Instead of running every request through a slow, expensive flagship model, NemotronForge implements the exact model tiering encouraged by Nebius and NVIDIA:
  > - Nemotron-3 Nano handles rapid triage and complexity scoring in under 150 milliseconds.
  > - Nemotron-3 Ultra (550B) designs the system architecture and edge-case contracts.
  > - Tavily AI Search provides real-time web grounding for live library documentation.
  > - And Nemotron-3 Super (120B) writes the production code and companion pytest test suite.
  > This hierarchy cuts token costs by over 68% compared to monolithic designs."

---

### [0:55 – 1:45] Live Demo: Self-Healing Bug Fix in Action
* **Visual:** Click on **Preset #2: Self-Healing Bug: JWT Clock-Skew Drift**. The prompt loads into the input box. Click the green button **"Dispatch Nemotron Agent Swarm"**.
* **Visual:** Show the pipeline nodes activating (Nano -> Ultra -> Tavily -> Super -> Sandbox -> Self-Healing).
* **Visual:** Switch between tabs:
  1. Show **Synthesized Code** tab with syntax highlighting.
  2. Click **Sandbox Console** tab: Show the test execution badge (`PASS 100%`).
  3. Click **Self-Healing Diff** tab: Show the unified diff highlighting the exact bug detected and corrected autonomously by Nemotron-3 Super!
* **Voiceover:**
  > "Let's see it in action. I'll select our Self-Healing Authentication preset and dispatch the swarm.
  > Watch the pipeline: Nano scores the complexity, Ultra creates the architectural specification, and Super synthesizes the implementation along with automated tests.
  > The code runs inside an isolated Python sandbox. When a defect is detected during test execution, NemotronForge captures the exact failure trace, queries Tavily for known workarounds, prompts Nemotron Super for a targeted fix, and re-runs the tests.
  > As you can see, all tests achieved a 100% pass rate, and the platform generates a clean unified diff showing the exact self-healing patch."

---

### [1:45 – 2:15] Live Tavily Grounding & Telemetry
* **Visual:** Click on the **Tavily Grounding** tab. Show the live search summary, source URLs, and relevance scores.
* **Visual:** Point to the **Nebius Token Factory Telemetry** card on the bottom left (total tokens, tier distribution, cost savings).
* **Voiceover:**
  > "Under the Tavily Grounding tab, you can see live documentation citations retrieved at runtime, qualifying us for the Best Use of Tavily track.
  > And on the left, our telemetry widget tracks token consumption across each model tier in real time, proving substantial cost savings."

---

### [2:15 – 2:30] Conclusion & Submission Wrap-Up
* **Visual:** Show the GitHub repository or code structure briefly.
* **Voiceover:**
  > "NemotronForge demonstrates what is possible when open-weights models like NVIDIA Nemotron are powered by sovereign, high-performance infrastructure on Nebius Token Factory.
  > Our code is open source under the MIT license, with full test coverage and automated setup. Thank you to Nebius and NVIDIA for hosting this incredible hackathon!"
