"""
<<<<<<< HEAD
Host Agent (Orchestrator)
=======
Host Agent (Orchestrator) (GIVEN - fully implemented)
>>>>>>> upstream/main
Root agent declaration for ADK Web testing

Available implementations:
1. agent.py - Basic SequentialAgent (default)
2. advanced_router_agent.py - Dynamic routing with callbacks (BONUS)
3. parallel_router_agent.py - Parallel execution with synthesis (BONUS)

<<<<<<< HEAD
Switch implementations via HOST_AGENT_MODE in .env:
- basic (default)
- advanced
- parallel
=======
To switch implementations, set HOST_AGENT_MODE environment variable:
- basic (default)
- advanced
- parallel

NOTE: root_agent is created at import time for ADK Web.
You must implement create_agent() before running `adk web`.
>>>>>>> upstream/main
"""

import os

<<<<<<< HEAD
=======
# Select which implementation to use
>>>>>>> upstream/main
AGENT_MODE = os.getenv("HOST_AGENT_MODE", "basic")

if AGENT_MODE == "advanced":
    from .advanced_router_agent import create_agent
    print("[HOST_AGENT] Using ADVANCED router with dynamic routing")
elif AGENT_MODE == "parallel":
    from .parallel_router_agent import create_agent
    print("[HOST_AGENT] Using PARALLEL router with concurrent execution")
else:
    from .agent import create_agent
    print("[HOST_AGENT] Using BASIC sequential router")

<<<<<<< HEAD
root_agent = create_agent()
=======
# Root agent - required for ADK Web
# This will raise NotImplementedError until you implement create_agent()
try:
    root_agent = create_agent()
except NotImplementedError:
    root_agent = None
    print("[WARN] host_agent: create_agent() not implemented yet."
          " Implement it in agents/host_agent/agent.py")
>>>>>>> upstream/main
