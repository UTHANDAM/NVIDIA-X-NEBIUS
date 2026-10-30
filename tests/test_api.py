import pytest
import asyncio
from unittest.mock import patch, AsyncMock
from backend.main import (
    get_health,
    get_models,
    get_presets,
    get_telemetry,
    execute_sandbox,
    generate,
    update_settings,
    SandboxExecuteRequest,
    GenerateRequest,
    SettingsUpdateRequest
)
from backend.config import settings

def test_health_endpoint():
    data = get_health()
    assert data["status"] == "healthy"
    assert "nebius_token_factory" in data
    assert "tavily_search" in data
    assert data["nebius_token_factory"]["endpoint"] == settings.NEBIUS_BASE_URL

def test_models_endpoint():
    data = get_models()
    assert data["provider"] == "Nebius Token Factory"
    assert len(data["models"]) >= 3
    model_ids = [m["id"] for m in data["models"]]
    assert any("Ultra" in m or "550b" in m for m in model_ids)
    assert any("super" in m or "120b" in m for m in model_ids)
    assert any("Nano" in m or "30B" in m for m in model_ids)

def test_presets_endpoint():
    data = get_presets()
    assert len(data) >= 4
    preset_ids = [p["id"] for p in data]
    assert "rate-limiter" in preset_ids
    assert "jwt-self-healing" in preset_ids
    assert "pydantic-v2-migration" in preset_ids

def test_telemetry_endpoint():
    data = get_telemetry()
    assert "total_tokens" in data
    assert "tier_distribution" in data
    assert "estimated_credit_savings_percent" in data

def test_sandbox_execution():
    req = SandboxExecuteRequest(
        code="def multiply(x, y):\n    return x * y\n",
        tests="from solution import multiply\ndef test_mul():\n    assert multiply(3, 4) == 12\n"
    )
    res = execute_sandbox(req)
    assert res["status"] == "PASSED"
    assert res["exit_code"] == 0

def test_settings_update():
    req = SettingsUpdateRequest(
        nebius_api_key="test_nebius_key",
        tavily_api_key="tvly-test123"
    )
    res = update_settings(req)
    assert res["status"] == "updated"
    # Restore clean state
    update_settings(SettingsUpdateRequest(nebius_api_key="", tavily_api_key=""))

def test_agent_orchestrator_generate_flow():
    req = GenerateRequest(
        prompt="Design a secure memory key-value cache with eviction.",
        enable_tavily=True,
        max_healing_rounds=2
    )
    mock_result = {
        "prompt": req.prompt,
        "final_status": "PASSED",
        "self_healed": True,
        "healing_iterations": 1,
        "code": "class Cache: pass",
        "tests": "def test_cache(): pass",
        "diff": "--- original\n+++ healed",
        "timeline": [
            {"stage": "triage", "status": "completed"},
            {"stage": "architecture", "status": "completed"},
            {"stage": "grounding", "status": "completed"},
            {"stage": "synthesis", "status": "completed"},
            {"stage": "sandbox", "status": "completed"},
            {"stage": "healing", "status": "completed"}
        ],
        "healing_history": [],
        "final_sandbox_result": {"status": "PASSED"},
        "telemetry_summary": {}
    }
    with patch("backend.main.agent_orchestrator.execute_task", new=AsyncMock(return_value=mock_result)):
        res = asyncio.run(generate(req))
        assert res["final_status"] == "PASSED"
        assert res["self_healed"] is True
        assert len(res["timeline"]) == 6
