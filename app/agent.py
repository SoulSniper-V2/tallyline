"""The Strands seam and the evidence coordinator used by the demo.

The evidence pass remains deterministic and authoritative, while a live
Strands model can inspect that pass through bounded typed tools and return a
short operator-facing readout. This gives the demo a real model-backed path
without giving a model authority to invent claims, submit a report, or move
money.
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


def _configured_model() -> Any | None:
    """Build the selected live model without ever reading a key into app state."""

    provider = os.getenv("TALLYLINE_MODEL_PROVIDER", "auto").lower()
    if provider not in {"auto", "gemini", "bedrock"}:
        raise RuntimeError("TALLYLINE_MODEL_PROVIDER must be auto, gemini, or bedrock.")

    gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if provider == "gemini" or (provider == "auto" and gemini_key):
        if not gemini_key:
            raise RuntimeError("Gemini live mode needs GEMINI_API_KEY or GOOGLE_API_KEY.")
        from strands.models.gemini import GeminiModel

        return GeminiModel(
            client_args={"api_key": gemini_key},
            model_id=os.getenv("TALLYLINE_MODEL_ID", "gemini-2.5-flash"),
            params={
                "temperature": 0.2,
                "max_output_tokens": 1024,
                "top_p": 0.9,
            },
        )

    model_id = os.getenv("TALLYLINE_MODEL_ID")
    if not model_id:
        return None
    from strands.models import BedrockModel

    model_config: dict[str, str] = {"model_id": model_id}
    if os.getenv("AWS_REGION"):
        model_config["region_name"] = os.environ["AWS_REGION"]
    return BedrockModel(**model_config)


def build_strands_agent() -> Any | None:
    """Build the real Strands coordinator when the SDK is importable.

    Construction is side-effect free. The model is invoked only by the
    explicit live route.
    """

    if not STRANDS_AVAILABLE or Agent is None:
        return None
    model = _configured_model()
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
    if os.getenv("TALLYLINE_AGENT_MODE", "local").lower() != "live":
        return "Strands • offline evidence pass"
    provider = os.getenv("TALLYLINE_MODEL_PROVIDER", "auto").lower()
    if provider == "auto" and (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")):
        provider = "gemini"
    return f"Strands • live {provider}"


def invoke_live_agent(case_id: str, approved_decisions: dict[str, str] | None = None) -> str:
    """Run the live Strands coordinator through the configured model.

    This is intentionally opt-in because it requires provider credentials and
    may incur model charges. A successful return is the only point at which
    the application labels a run as live.
    """

    agent = build_strands_agent()
    if agent is None:
        raise RuntimeError("The Strands SDK is not available in this environment.")
    decisions = ", ".join(f"{key}: {value}" for key, value in (approved_decisions or {}).items()) or "none"
    response = agent(
        f"""Review synthetic grant closeout case {case_id}. You must use the reconcile_evidence tool and then the draft_supported_report tool. Summarize in under 80 words for an operator: the supported totals, any claim that needs human review, and the consent boundary. Use only tool-returned evidence. Never invent a number, submit anything, or move money. Current approved decisions: {decisions}."""
    )
    return str(response).strip()
