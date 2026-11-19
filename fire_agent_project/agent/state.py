from typing import TypedDict, Any

class AgentState(TypedDict, total=False):
    user_request: str
    session_id: str
    intent: dict
    plan: list
    selected_tools: list
    tool_results: dict
    assessment: dict
    constraints_satisfied: bool | None
    retry_count: int
    max_retries: int
    final_answer: str
    execution_logs: list
    events: list
    candidates: list
    memory: list
    error: str | None
    llm_status: dict
