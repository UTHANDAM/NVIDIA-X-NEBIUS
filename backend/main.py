"""
NemotronForge FastAPI Backend Gateway.
Exposes REST APIs for multi-model orchestrator, sandbox runner, telemetry, and live settings.
Serves the high-fidelity interactive developer dashboard.
"""
import os
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from backend.config import settings
from backend.nebius_client import nebius_client
from backend.tavily_client import tavily_client
from backend.sandbox_runner import sandbox_runner
from backend.agent_orchestrator import agent_orchestrator
from backend.presets import PRESETS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Autonomous Multi-Tier Agentic Software Engineering Platform powered by NVIDIA Nemotron on Nebius Token Factory."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# Request & Response Models
# -------------------------------------------------------------
class GenerateRequest(BaseModel):
    prompt: str
    enable_tavily: bool = True
    max_healing_rounds: int = 3

class SandboxExecuteRequest(BaseModel):
    code: str
    tests: str
    timeout_seconds: Optional[int] = 15

class SettingsUpdateRequest(BaseModel):
    nebius_api_key: Optional[str] = None
    tavily_api_key: Optional[str] = None

# -------------------------------------------------------------
# API Endpoints
# -------------------------------------------------------------
@app.get("/api/health")
def get_health() -> Dict[str, Any]:
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "nebius_token_factory": {
            "endpoint": settings.NEBIUS_BASE_URL,
            "is_live": nebius_client.is_live,
            "models": {
                "ultra": settings.MODEL_ULTRA,
                "super": settings.MODEL_SUPER,
                "nano": settings.MODEL_NANO
            }
        },
        "tavily_search": {
            "is_live": tavily_client.is_live,
            "endpoint": settings.TAVILY_BASE_URL
        }
    }

@app.get("/api/models")
def get_models() -> Dict[str, Any]:
    return {
        "provider": "Nebius Token Factory",
        "models": [
            {
                "id": settings.MODEL_ULTRA,
                "name": "NVIDIA Nemotron-3 Ultra (550B)",
                "tier": "Cognitive Architecture",
                "role": "Master System Architect, structural decomposition, edge-case theorem proving.",
                "context_window": "128k",
                "status": "Ready"
            },
            {
                "id": settings.MODEL_SUPER,
                "name": "NVIDIA Nemotron-3 Super (120B)",
                "tier": "Code Synthesis & Self-Healing",
                "role": "High-throughput code generator, test synthesizer, differential patch creator.",
                "context_window": "64k",
                "status": "Ready"
            },
            {
                "id": settings.MODEL_NANO,
                "name": "NVIDIA Nemotron-3 Nano (30B)",
                "tier": "Fast Triage & Safety",
                "role": "Sub-150ms intent categorization, token budget routing, syntax safety filter.",
                "context_window": "32k",
                "status": "Ready"
            }
        ]
    }

@app.get("/api/presets")
def get_presets():
    return PRESETS

@app.get("/api/telemetry")
def get_telemetry():
    return nebius_client.get_telemetry_summary()

@app.post("/api/settings")
def update_settings(req: SettingsUpdateRequest):
    if req.nebius_api_key is not None:
        nebius_client.set_api_key(req.nebius_api_key)
    if req.tavily_api_key is not None:
        tavily_client.set_api_key(req.tavily_api_key)
    
    return {
        "status": "updated",
        "nebius_is_live": nebius_client.is_live,
        "tavily_is_live": tavily_client.is_live
    }

@app.post("/api/generate")
async def generate(req: GenerateRequest):
    if not req.prompt or not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt must not be empty.")
    
    try:
        result = await agent_orchestrator.execute_task(
            user_prompt=req.prompt.strip(),
            enable_tavily=req.enable_tavily,
            max_healing_rounds=req.max_healing_rounds
        )
        return result
    except Exception as e:
        logger.error(f"Generation failure: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/execute-sandbox")
def execute_sandbox(req: SandboxExecuteRequest):
    if not req.code or not req.tests:
        raise HTTPException(status_code=400, detail="Both code and test contents are required.")
    
    res = sandbox_runner.execute_test(
        code_content=req.code,
        test_content=req.tests,
        timeout_seconds=req.timeout_seconds or 15
    )
    return res

# -------------------------------------------------------------
# Embedded Interactive UI Dashboard
# -------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def index():
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h2>NemotronForge Backend is running! UI loading...</h2>")
