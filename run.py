"""
NemotronForge Entrypoint Launcher.
Run with: python run.py
Serves the API and interactive dashboard at http://localhost:8000
"""
import uvicorn
from backend.config import settings

if __name__ == "__main__":
    print(f"============================================================")
    print(f"  Launching {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"  Autonomous Self-Healing AI Engineer")
    print(f"  NVIDIA Nemotron x Nebius Token Factory & Tavily Grounding")
    print(f"  Interactive Dashboard: http://{settings.HOST}:{settings.PORT}")
    print(f"============================================================")
    uvicorn.run(
        "backend.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=False
    )
