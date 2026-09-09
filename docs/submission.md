# Agents for Humans submission draft

## One-line pitch

Tallyline is the Good Neighbor agent that turns a small nonprofit's scattered closeout files into a traceable grant report—without letting an AI invent a number, publish a story without consent, or submit on the operator's behalf.

## Devpost description

Small community organizations are often asked to prove impact with the least structured data: a spreadsheet, a few receipts, a program log, and story notes in different folders. Tallyline is an evidence-first grant closeout agent. It extracts the award's reporting lines, reconciles deterministic totals, maps each report claim to a source, and drafts only what the files can support.

The key artifact is the claim ledger. It makes supported, needs-review, and blocked claims visible. A duplicate activity row is removed before totaling. A budget variance stays in the human queue until someone explains it. A beneficiary note without publication consent never enters the narrative. The operator can resolve the final calls and export a Markdown report plus evidence index, but Tallyline has no submission, email, payment, or money-moving tool.

The repository includes a runnable FastAPI app, synthetic fixtures, tests, an architecture diagram, and an MIT license. The local demo is deterministic and reviewable. `app/agent.py` contains the Strands Agents SDK coordinator seam with bounded tools; a future Bedrock AgentCore deployment is an explicit extension point, not represented as a completed deployment in this submission.

## Five-minute demo script

**0:00–0:35 — Scene.** Open the app. Say: “This is a synthetic grant closeout for a small community organization. The files are not clean enough to trust a polished paragraph.” Point to the four-source drawer and the award slip.

**0:35–1:20 — Run.** Click “Run reconciliation.” Let the route fill from Read to Reconcile to Trace. Explain that the local Strands-labelled pass is deterministic for this demo, so the exact decision behavior is inspectable.

**1:20–2:20 — Claim ledger.** Point out 128 households, 124 kits, and 3 workshops. Expand the household line and show that the repeated `event_id` was removed before totaling. Expand spend: $15,940 of $18,000 is known, so the $2,060 difference is not silently treated as spent.

**2:20–3:25 — Human queue.** Show the three decisions: explain the finance variance, keep the non-consented note private, and confirm period coverage. Click each action. Explain that approval changes the packet state; it does not mutate source files or submit anything.

**3:25–4:10 — Draft packet.** Show the report updating as decisions resolve. Point to the status line and the note that unsupported/non-consented narrative is excluded. Click “Export .md” and open the generated evidence index.

**4:10–4:45 — Architecture and safety.** Show the diagram or repository. Explain FastAPI → deterministic service → typed Strands tools → claim ledger → human handoff. Mention that Bedrock AgentCore is a documented production path, not a claim about this local run.

**4:45–5:00 — Close.** “Tallyline does not write the story for the operator. It makes the evidence travel with the story, and keeps the last call human.”

## Judge lens

These are design choices informed by the published rubric and judge roles; they are not claims about any individual judge's private preferences.

- **Technical implementation:** reproducible local run, direct JSON endpoints, typed Strands tools, deterministic dedupe and totals, explicit side-effect boundary, and tests for the important uncertainty paths.
- **Design:** an archive/finding-aid workbench rather than a generic AI chat or card dashboard; the first viewport shows the mechanism, and source/status details are one interaction away.
- **Potential impact:** the workflow targets a real burden in grant reporting: oversight needs financial, compliance, and project/impact evidence, while outputs are easier to report than outcomes. The demo avoids claiming measured impact for a real organization.
- **Creativity/originality:** the claim ledger is the product, not prose generation. Consent and unsupported evidence are first-class states.
- **Presentation:** the demo uses one synthetic case with a visible duplicate, variance, and consent boundary so the agent's judgment can be inspected in under five minutes.

## Competition disclosure

This repository's Tallyline application, fixtures, tests, docs, and interface were created as a new hackathon build during the competition's stated coding window. No pre-existing application code is being presented as new work. The general problem framing and the creator's prior skills/knowledge predate this build; those are not represented as prior software or prior competition submission. All demo data is synthetic and authored for this repository.

## Submission checklist

- [x] Public code repository contents: source, fixture data, tests, setup, docs
- [x] MIT license
- [x] README with run instructions
- [x] Architecture diagram
- [x] Strands Agents SDK dependency and typed agent seam
- [x] Human-in-the-loop and no-irreversible-action boundary
- [ ] Public YouTube/Vimeo demo link — add only after recording and verifying visibility
- [ ] AWS Builder ID — complete on the submitter account
- [x] Final public repository URL and commit — `https://github.com/SoulSniper-V2/tallyline` (`551f00c`)
- [ ] Optional builder.aws post with “Agents for Humans” in the title — only if actually published
