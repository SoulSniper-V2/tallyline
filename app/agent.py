"""The Strands seam and the offline coordinator used by the demo.

The product intentionally keeps the deterministic evidence pass separate from
model generation. This makes the local demo reviewable and means the same
typed tools can later be hosted behind Bedrock AgentCore without giving a
model authority to submit a report or move money.
"""

from __future__ import annotations

import json
import os
from typing import Any

try:  # Strands is a required project dependency, but keep imports diagnosable.
    from strands import Agent, tool

    STRANDS_AVAILABLE = True
except ImportError:  # pragma: no cover - exercised only in minimal environments.
    Agent = None  # type: ignore[assignment,misc]
    STRANDS_AVAILABLE = False

    def tool(function: Any) -> Any:
        return function


@tool
def reconcile_evidence(case_id: str) -> str:
    """Return the reconciled claim ledger for a case.

    The deterministic implementation remains the source of truth. Keeping it
    behind a typed Strands tool means a live model can request the same bounded
    operation without receiving a write or submission capability.
    """

    from .service import run_case

    result = run_case()
    if case_id != result.summary.award_id:
        return json.dumps({"error": "unknown case", "case_id": case_id})
    return json.dumps({
        "summary": result.summary.model_dump(),
        "claims": [claim.model_dump() for claim in result.claims],
        "decisions": [decision.model_dump() for decision in result.decisions],
    })


@tool
def draft_supported_report(case_id: str, approved_decisions: str = "none") -> str:
    """Return a report draft built from the claim ledger and approvals."""

    from .service import export_markdown, run_case

    result = run_case()
    if case_id != result.summary.award_id:
        return "Unknown case; no draft produced."
    return export_markdown(result) + f"\n\nAgent context: approved decisions = {approved_decisions}."


def build_strands_agent() -> Any | None:
    """Build the real Strands coordinator when the SDK is importable.

    No model call happens here. The optional provider is visible in the UI so
    reviewers can distinguish the local deterministic path from a live model.
    """

    if not STRANDS_AVAILABLE or Agent is None:
        return None
    model = None
    model_id = os.getenv("TALLYLINE_MODEL_ID")
    if model_id:
        from strands.models import BedrockModel

        model_config: dict[str, str] = {"model_id": model_id}
        if os.getenv("AWS_REGION"):
            model_config["region_name"] = os.environ["AWS_REGION"]
        model = BedrockModel(**model_config)
    return Agent(
        model=model,
        name="Tallyline Coordinator",
        system_prompt=(
            "You coordinate grant closeout evidence. Use only typed tools. "
            "Never invent claims, submit a report, send email, or move money. "
            "Escalate missing evidence and consent decisions to a human."
        ),
        tools=[reconcile_evidence, draft_supported_report],
    )


def provider_label() -> str:
    return "Strands • local deterministic pass"


def invoke_live_agent(case_id: str, approved_decisions: dict[str, str] | None = None) -> str:
    """Run the live Strands coordinator through the configured Bedrock model.

    This is intentionally opt-in because it requires AWS credentials and may
    incur model charges. A successful return is the only point at which the
    application labels a run as live.
    """

    agent = build_strands_agent()
    if agent is None:
        raise RuntimeError("The Strands SDK is not available in this environment.")
    decisions = ", ".join(f"{key}: {value}" for key, value in (approved_decisions or {}).items()) or "none"
    response = agent(
        f"""Review synthetic grant closeout case {case_id}. You must use the reconcile_evidence tool and then the draft_supported_report tool. Summarize in under 100 words: the supported totals, any claim that needs human review, and the consent boundary. Never invent evidence, submit anything, or move money. Current approved decisions: {decisions}."""
    )
    return str(response).strip()
