# Tallyline verification record

Checked September 8, 2026 from the project root.

## Proven

- `uv sync --extra dev` completed and installed `strands-agents==1.55.0`, its Gemini provider extra, FastAPI, Uvicorn, pytest, and Playwright.
- `uv run python -c 'from app.agent import ...; build_strands_agent()'` imported and constructed a real `strands.Agent`.
- The application has an explicit credential-gated live path: `TALLYLINE_AGENT_MODE=live` invokes the Strands coordinator through the configured Gemini or Bedrock provider and labels the result live only after a successful response.
- A direct live probe with `TALLYLINE_MODEL_PROVIDER=gemini` and `gemini-2.5-flash` completed through Strands. The server log showed `Tool #1: reconcile_evidence` and `Tool #2: draft_supported_report`; the returned readout stayed within the synthetic ledger: 128 households, 124 kits, 3 workshops, $15,940 of $18,000, a $2,060 variance for human review, and missing publication consent.
- A live `POST /api/run` returned HTTP 200 with `agent_mode: live`, provider `Strands • live gemini`, and a non-empty advisory `agent_note`. No API key is stored in the repository.
- `uv run pytest -q` passed: 5 tests (one existing Starlette deprecation warning from the test client).
- Direct HTTP smoke checks passed for `/api/health`, `/api/case`, `/api/decisions/approve`, and `/api/export`.
- Playwright browser verification passed at 1440px and 390px: 5 ledger rows, 128 households, expandable claim detail, decision approvals down to zero open decisions, Markdown export, no console errors, and no horizontal overflow.
- `docs/architecture.svg` and the JSON fixtures parse successfully.
- Visual review captures: `.impeccable/review/desktop.png` and `.impeccable/review/mobile.png`.
- `outputs/tallyline-demo.mp4` was generated from the running FastAPI UI with a scripted Playwright walkthrough, a visible live Gemini/Strands readout, narration, H.264/AAC encoding, and a verified duration of 227.28 seconds at 1440×900. Full decode completed without errors; the closing frame includes the model/safety handoff card.
- The repository was pushed to `https://github.com/SoulSniper-V2/tallyline` and independently verified public through GitHub metadata.

## Not claimed

- No AWS account, Bedrock model invocation, AgentCore deployment, or hosted app URL was verified in this workspace. The Bedrock/AgentCore path remains implemented and documented, not claimed as deployed.
- No public YouTube/Vimeo video URL, AWS Builder ID, or builder.aws post was created. Those checklist items remain deliberately open in `docs/submission.md`; the local MP4 is ready for upload.
- Fixture outputs and beneficiary notes are synthetic and should not be presented as measured real-world impact.
