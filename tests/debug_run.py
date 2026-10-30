import asyncio
import time
from backend.agent_orchestrator import agent_orchestrator

async def main():
    print("1. Starting main...", flush=True)
    res = await agent_orchestrator.execute_task("Build a memory store", enable_tavily=False, max_healing_rounds=0)
    print("2. Finished execute_task!", flush=True)
    print("Status:", res["final_status"], flush=True)

if __name__ == "__main__":
    asyncio.run(main())
