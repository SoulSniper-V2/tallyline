# Tallyline

**Evidence-first grant closeout for small community organizations.**

Tallyline turns an award brief, activity log, finance export, and story notes into a funder-ready closeout draft whose claims stay attached to their evidence. It shows the operator what is supported, what needs review, and what is blocked by consent or missing context. The operator resolves the final decisions; Tallyline does not submit, email, pay, or move money.

This is a synthetic local demo for the Agents for Humans Hackathon. No beneficiary data is real.

## Run it

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/).

On macOS, double-click `START_TALLYLINE.command`. It installs the locked dependencies, starts the local server, and opens the correct browser URL. Do not double-click `app/static/index.html`: the UI needs the FastAPI server for its CSS, JavaScript, and API.

```bash
uv sync --extra dev
uv run uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000. The page runs the synthetic case on load. Use the explicit action to replay it, expand a claim to inspect its source note, resolve the three human decisions, and export the Markdown packet.

Run the test suite:

```bash
uv run pytest -q
```

## What the demo proves

- The activity pass deduplicates a repeated `event_id` before totaling outputs: 128 households, 124 kits, and 3 workshops.
- Finance totals reconcile to $15,940 against the $18,000 award and stay in the human queue as a $2,060 variance until the operator explains it.
- A non-consented story remains blocked; the draft uses only the consented note.
- The same state is available through direct JSON APIs: `GET /api/case`, `POST /api/run`, `POST /api/decisions/approve`, `POST /api/reset`, and `GET /api/export`.

## Agent architecture

The default local path is deterministic so a reviewer can inspect the exact behavior without an AWS account or model key. `app/agent.py` contains a real Strands `Agent`, two bounded typed tools, and an opt-in live Bedrock invocation path. Set `TALLYLINE_AGENT_MODE=live`, `AWS_REGION`, and `TALLYLINE_MODEL_ID` with valid AWS credentials to make `/api/run` perform the live agent pass; the app returns an error rather than labeling a failed call as live. `app/service.py` owns the evidence ledger and report assembly. Bedrock AgentCore is a compatible hosting path, but it is not required and is not claimed as deployed here.

Example live probe (use a model enabled in your AWS region; model calls may incur cost):

```bash
TALLYLINE_AGENT_MODE=live AWS_REGION=YOUR_REGION TALLYLINE_MODEL_ID=YOUR_MODEL_ID \
  uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
curl -X POST http://127.0.0.1:8000/api/run
```

See [docs/architecture.svg](docs/architecture.svg) and [docs/submission.md](docs/submission.md).

## Project status and disclosure

The application, fixture data, tests, documentation, and visual direction in this repository were created for this hackathon build during the stated competition window. The underlying idea—evidence-first reporting with human consent boundaries—is the build thesis, not evidence of a deployed product. See the disclosure section in [docs/submission.md](docs/submission.md) for the exact competition wording.

## License

MIT. See [LICENSE](LICENSE).
