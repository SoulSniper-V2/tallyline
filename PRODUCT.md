# Tallyline — Product Contract

## Status

Working product brief for the Agents for Humans Hackathon build. Product facts below are either explicit decisions for this build or marked as an inference from the supplied hackathon brief and bounded research.

## Product in one sentence

Tallyline is a Good Neighbor agent that turns a small nonprofit's award letter, program log, finance export, and story notes into a funder-ready grant closeout packet whose claims are traceable to evidence and whose unresolved choices stay with a human.

## Audience

- Primary: the program or operations lead at a small community organization who owns grant reporting but does not have a dedicated grants team.
- Secondary: a volunteer bookkeeper or executive director reviewing the packet before it reaches a funder.

## Problem

Closeout reporting is not just writing. The operator has to reconcile outputs, spending, deadlines, and narrative evidence across files that were never designed to line up. A polished paragraph can still be wrong if a number is stale, a category is mismatched, or a beneficiary story was recorded without permission.

## Promise

Show the operator what can be supported, where it came from, and what needs a decision before they copy anything into a funder portal.

## Core workflow

1. Ingest a synthetic award brief, activity log, finance export, and story notes.
2. Extract reporting requirements and normalize the evidence into a claim ledger.
3. Reconcile deterministic totals and compare them with the award's targets and budget.
4. Draft only supported narrative; flag unsupported or consent-sensitive claims.
5. Ask the operator for the smallest set of human decisions.
6. Export a report plus an evidence index. Tallyline never submits, moves money, or invents impact.

## What makes this original

The artifact is the claim ledger, not an AI-written report. Every sentence-level claim has a status (supported, needs review, or blocked), a source reference, and a human decision boundary. The experience makes uncertainty visible instead of hiding it behind a confidence score.

This is intentionally separate from volunteer/stock allocation, generic pre-award grant discovery, and irreversible operations automation observed in the competition scan.

## Demo scenario

Synthetic award: Neighborhood Cooling Kits, $18,000, with targets for 120 households reached, 120 kits distributed, and 3 cooling workshops. The fixture contains 128 logged households, 124 kits, 3 workshops, $15,940 in reconciled expenses, one duplicate-looking log row resolved by the deterministic pass, and two story notes: one consented, one blocked. The correct demo outcome is a near-complete packet with three human decisions, not a fabricated perfect score.

## Non-goals

- No funder submission, email, payment, bank connection, or money movement.
- No claim that the sample data is a real nonprofit outcome.
- No live AWS, Bedrock, or AgentCore deployment claim until separately performed and verified.
- No private beneficiary details in the demo; all fixture data is synthetic.

## Technical shape

- Python 3.12, FastAPI, and a small static browser UI.
- A provider-neutral domain service that runs deterministically offline for reviewability.
- A Strands Agents SDK adapter with a root `Agent`, typed tools, and named specialist agents; the adapter is optional at runtime so the demo remains runnable without AWS credentials or a model key.
- Optional production path documented for Bedrock/AgentCore, with session state and tool permissions kept explicit.
- JSON APIs for run, approve, reset, and export so the behavior can be directly tested.

## Visual thesis

Calm operations notebook: warm paper, ink-black type, signal-orange decisions, and a thin route line showing evidence moving through the workflow. The first viewport must communicate working state, the claim ledger, and the human queue without dashboard card-grid sludge.

## Success criteria for this build

- A reviewer can run the synthetic case in under one minute and understand why each claim is or is not usable.
- The UI makes a blocked story and a budget mismatch legible without requiring a second page.
- The API and tests demonstrate the same boundaries shown in the UI.
- README, architecture diagram, license, demo script, disclosure, and research artifact are present.
