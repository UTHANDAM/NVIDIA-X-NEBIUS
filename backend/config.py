"""
Configuration settings for NemotronForge.
Supports Nebius Token Factory, NVIDIA Nemotron models, and Tavily Search API.
"""
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "NemotronForge"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    PORT: int = 8000
    HOST: str = "127.0.0.1"

    # Nebius Token Factory Settings
    # Base URL for OpenAI-compatible Nebius Token Factory API
    NEBIUS_BASE_URL: str = os.getenv("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.com/v1/")
    NEBIUS_API_KEY: str = os.getenv("NEBIUS_API_KEY", "")

    # NVIDIA Nemotron Models Hosted on Nebius Token Factory
    # Tier 1: Ultra (Flagship, Deep Architectural Reasoning, Multi-step Synthesis)
    MODEL_ULTRA: str = os.getenv("MODEL_ULTRA", "nvidia/Nemotron-3-Ultra-550b-a55b")
    # Tier 2: Super (Code Generation, Test Writing, Differential Refactoring)
    MODEL_SUPER: str = os.getenv("MODEL_SUPER", "nvidia/nemotron-3-super-120b-a12b")
    # Tier 3: Nano (Rapid Routing, Intent Classification, Fast Validation)
    MODEL_NANO: str = os.getenv("MODEL_NANO", "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B")
    # Fallback / General Model
    MODEL_LLAMA_NEMOTRON: str = os.getenv("MODEL_LLAMA_NEMOTRON", "nvidia/Llama-3.1-Nemotron-70B-Instruct")

    # Tavily Search API
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    TAVILY_BASE_URL: str = "https://api.tavily.com/search"

    # Execution Sandbox Settings
    SANDBOX_TIMEOUT_SECONDS: int = 15
    MAX_HEALING_ITERATIONS: int = 3
    SANDBOX_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sandbox_runs")

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
