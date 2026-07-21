"""
Part 2a: Customer Data Agent (15 points)

Create an ADK Agent that manages customer and ticket data via McpToolset.

This agent should:
  - Use the Gemini model from agents_config
  - Have a descriptive instruction telling the LLM its role and capabilities
  - Include the customer data McpToolset so it can access customer/ticket data
<<<<<<< HEAD
python -m google.adk.cli web agents/customer_data_agent

The McpToolset auto-discovers tools from the MCP server — no manual wrapper functions needed.
=======

The McpToolset auto-discovers tools from the MCP server — no manual wrappers needed.
>>>>>>> upstream/main
You configure which tools the agent can access via the tool_filter in the toolset.

Requirements:
  - create_agent() returns a configured google.adk.agents.Agent (5 pts)
  - Agent has a detailed instruction string (5 pts)
  - Agent uses create_customer_data_toolset() (5 pts)

Example instruction topics to cover:
  - The agent's role (Customer Data specialist)
  - What tools are available (customer lookup, ticket management, statistics)
  - How to handle requests (parse, use tools, format response)
  - Response style (precise, data-driven)
"""

import sys
import os
import logging

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents import Agent
from shared.agents_config import GEMINI_MODEL
from shared.mcp_toolset import create_customer_data_toolset

<<<<<<< HEAD
=======
# Configure logging for this agent
>>>>>>> upstream/main
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [CUSTOMER_DATA_AGENT] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

<<<<<<< HEAD
CUSTOMER_DATA_INSTRUCTION = """
You are the Customer Data Agent — an isolated data lookup and records clerk for the
customer support platform. Your sole purpose is to retrieve, create, and update customer
and ticket records in the database. You do NOT provide troubleshooting advice, policy
guidance, or general customer support. You are a backend data specialist that other
agents and operators rely on for accurate, factual database operations.

## Your Role
- Act as a dedicated data clerk with broad access to customer and ticket records.
- Fulfill data requests precisely: look up records, list filtered results, create or
  update entries, and return statistics when asked.
- Stay strictly within your data-management scope. If a request is outside database
  operations (e.g., "how do I reset my password?"), respond that you only handle
  customer and ticket data operations and cannot provide support guidance.

## Available Capabilities (via MCP tools)
You have access to the following tool categories:

**Customer Operations**
- get_customer: Retrieve a single customer record by ID
- list_customers: List customers with optional filters
- add_customer: Create a new customer record
- update_customer: Modify an existing customer record
- disable_customer: Deactivate a customer account (admin operation)
- activate_customer: Reactivate a disabled customer account (admin operation)

**Ticket Operations**
- get_ticket: Retrieve a single support ticket by ID
- list_tickets: List tickets with optional filters (status, priority, customer)
- create_ticket: Open a new support ticket for a customer
- update_ticket_status: Change a ticket's status (open, in_progress, resolved, closed)
- update_ticket_priority: Change a ticket's priority (low, medium, high, critical)

**Statistics and Search**
- get_ticket_stats: Aggregate ticket counts by status and priority
- get_customer_stats: Aggregate customer counts and activity metrics
- search_tickets: Full-text search across ticket subjects and descriptions

## How to Handle Requests
1. **Parse the request** — Identify whether the user needs a customer lookup, ticket
   operation, statistics, or a combination. Extract IDs, filters, and field values.
2. **Select the right tool(s)** — Call the minimum number of tools needed. For example,
   look up a customer first if you need their ID before creating a ticket.
3. **Execute and verify** — Use the MCP tools to fetch or modify data. If a record is
   not found, report that clearly rather than guessing.
4. **Format the response** — Present results in a structured, readable format with
   relevant fields (IDs, names, statuses, dates). Include counts when listing records.

## Response Style
- Be precise, concise, and data-driven. Lead with the answer, then supporting details.
- Use consistent formatting: label fields clearly (e.g., "Customer ID: 42").
- When listing multiple records, summarize the count and show key fields for each.
- Never fabricate data. If a tool returns no results or an error, state that honestly.

## Error Handling
- If a tool call fails or returns an error, relay the error message clearly and suggest
  what information might be missing (e.g., "Customer ID 999 was not found").
- If required parameters are missing from the request, ask for them before calling tools.
- Do not retry failed operations silently; report the failure and let the caller decide.
""".strip()


def create_agent() -> Agent:
    """Create and return the configured Customer Data Agent.

    Returns:
        Configured Agent instance with model, instruction, and MCP toolset.
    """
    logger.info("Creating Customer Data Agent")
    return Agent(
        model=GEMINI_MODEL,
        name='customer_data_agent',
        instruction=CUSTOMER_DATA_INSTRUCTION,
        tools=[create_customer_data_toolset()],
=======

def create_agent() -> Agent:
    """
    Create the Customer Data Agent.

    TODO: Create and return an Agent instance with:
      1. model=GEMINI_MODEL
      2. name='customer_data_agent'
      3. instruction=<your detailed instruction string>
      4. tools=[create_customer_data_toolset()]

    The McpToolset automatically discovers all filtered tools from the MCP
    server. You pass the toolset instance in the tools list — ADK handles
    the rest.

    Example:
        return Agent(
            model=GEMINI_MODEL,
            name='customer_data_agent',
            instruction=\"\"\"
            You are the Customer Data Agent...
            Your capabilities:
            - Retrieve customer information by ID
            - List customers with filters
            ...
            \"\"\",
            tools=[create_customer_data_toolset()],
        )

    Returns:
        Configured Agent instance
    """
    raise NotImplementedError(
        "TODO: Create the Customer Data Agent with model, name, instruction, and tools. "
        "Use tools=[create_customer_data_toolset()] to attach the MCP toolset."
>>>>>>> upstream/main
    )
