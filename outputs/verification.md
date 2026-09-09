# Tallyline verification record

Checked September 8, 2026 from the project root.

## Proven

- `uv sync --extra dev` completed and installed `strands-agents==1.55.0`, FastAPI, Uvicorn, pytest, and Playwright.
- `uv run python -c 'from app.agent import ...; build_strands_agent()'` imported and constructed a real `strands.Agent`.
- The application now has an explicit credential-gated live path: `TALLYLINE_AGENT_MODE=live` invokes the Strands coordinator through Bedrock and labels the result live only after a successful response.
- `uv run pytest -q` passed: 3 tests.
- Direct HTTP smoke checks passed for `/api/health`, `/api/case`, `/api/decisions/approve`, and `/api/export`.
- Playwright browser verification passed at 1440px and 390px: 5 ledger rows, 128 households, expandable claim detail, decision approvals down to zero open decisions, Markdown export, no console errors, and no horizontal overflow.
- `docs/architecture.svg` and the JSON fixtures parse successfully.
- Visual review captures: `.impeccable/review/desktop.png` and `.impeccable/review/mobile.png`.
- `outputs/tallyline-demo.mp4` was generated from the running FastAPI UI with a scripted Playwright walkthrough, narration, H.264/AAC encoding, and a verified duration of 180.08 seconds at 1440×900.
- The repository was pushed to `https://github.com/SoulSniper-V2/tallyline` and independently verified public through GitHub metadata.

## Not claimed

- No AWS account, Bedrock model invocation, AgentCore deployment, or hosted app URL was verified in this workspace.
- Therefore, the live Strands/Bedrock path is implemented but not live-verified in this workspace.
- No public YouTube/Vimeo video URL, AWS Builder ID, or builder.aws post was created. Those checklist items remain deliberately open in `docs/submission.md`; the local MP4 is ready for upload.
- Fixture outputs and beneficiary notes are synthetic and should not be presented as measured real-world impact.
