"""
Pre-engineered Challenge Scenarios for NemotronForge.
Designed for 1-click evaluation by hackathon judges and developers.
"""
from typing import List, Dict, Any

PRESETS: List[Dict[str, Any]] = [
    {
        "id": "rate-limiter",
        "title": "Distributed Concurrency Rate Limiter",
        "track": "Coding & Agentic Engineering",
        "badge": "High Concurrency",
        "description": "Architect and implement a thread-safe Token Bucket rate limiter with sliding window semantics, burst capacity limits, and automatic replenishment.",
        "prompt": "Create a thread-safe Token Bucket rate limiter in Python. It must support configurable refill rate (tokens/sec), maximum bucket capacity, and an acquire() method that returns True if tokens were available or False otherwise. Include boundary checks and full pytest suite.",
        "demonstrates": "Nemotron-3 Ultra architectural design + Nemotron-3 Super thread-safe code synthesis."
    },
    {
        "id": "jwt-self-healing",
        "title": "Self-Healing Bug: JWT Clock-Skew Drift",
        "track": "Best Apps and Agents",
        "badge": "Autonomous Self-Healing",
        "description": "Demonstrates the live self-healing loop. A tricky authentication timestamp defect is detected by the sandbox test runner and autonomously corrected by Nemotron-3 Super.",
        "prompt": "Build an authentication token validator class `AuthValidator` that validates user sessions, verifies expiry timestamps against UTC time, and handles leeway clock skew (5 seconds). Ensure it rejects empty tokens, malformed headers, and expired payloads.",
        "demonstrates": "Autonomous error detection, stack-trace parsing, and iterative zero-shot self-healing."
    },
    {
        "id": "pydantic-v2-migration",
        "title": "Pydantic V1 -> V2 Migration Grounded by Tavily",
        "track": "Tavily Bonus Award ($3,000)",
        "badge": "Tavily Web Grounding",
        "description": "Queries the live Tavily search API to ground Nemotron in the latest Pydantic V2 migration specifications, replacing deprecated `.dict()` and `@validator` methods.",
        "prompt": "Migrate a legacy user data schema from Pydantic V1 to Pydantic V2. Query current documentation via Tavily, implement custom field validators using `@field_validator`, and output serialized dictionaries with `.model_dump()`. Include comprehensive unit tests.",
        "demonstrates": "Runtime Tavily API call + NVIDIA Nemotron-3 Super schema transformation."
    },
    {
        "id": "resilient-async-pipeline",
        "title": "Async Event Pipeline with Circuit Breaker",
        "track": "Best Apps and Agents",
        "badge": "Fault Tolerance",
        "description": "Designs an asynchronous pipeline with exponential backoff retries, dead-letter queue (DLQ), and circuit breaker state transitions (CLOSED, OPEN, HALF-OPEN).",
        "prompt": "Build an asynchronous worker pipeline in Python with a Circuit Breaker pattern. It must track failure thresholds, transition between CLOSED/OPEN/HALF-OPEN states, and support an isolated Dead-Letter Queue (DLQ) for poisoned messages.",
        "demonstrates": "Complex multi-component architecture with Nemotron-3 Ultra + companion async pytest verification."
    }
]
