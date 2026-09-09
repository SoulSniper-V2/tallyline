# Tallyline visual system

## North star

Tallyline should feel like a public archive finding aid in active use: precise enough to trust, human enough to show where judgment still belongs. The surface is an evidence route, not an AI chat window or a dashboard of decorative cards.

## Tokens

- Canvas: fog green `#d9ded6`; deep canvas `#c8d0c7`.
- Paper: butter `#f4f0df`; bright paper `#fbf8ea`.
- Ink: deep green-black `#13211f`; supporting text `#53615b`.
- Signal: burnt orange `#db6c3b` / deep orange `#a7442a`.
- Proof: chartreuse `#d6e155`; source blue `#315ca8`.
- Rules: one-pixel ink lines at 20% or 44% opacity.

## Type and rhythm

System sans for display and readable content; system monospace for archive labels, source names, status, and evidence notes. Display type is large, close-set, and left aligned. Functional text stays at or above 11px; labels are uppercase and short. Use generous region spacing and thin rules instead of nested containers.

## Components

- Case slip: butter-paper document with a light inset rule and slight physical rotation; contains award identity and synthetic-data stamp.
- Route: four fixed stops with a single orange progress line; completed nodes are ink-filled, active is paper with orange edge.
- Claim ledger: ruled table; each row has value, status pill, source, and an expandable “why this status” detail.
- Decision queue: open questions are orange labels with one human action; resolved choices become a green text receipt.
- Draft packet: a single paper sheet, never a grid of cards; statuses remain visible in the report.

## Interaction and states

The run action communicates tracing with a brief busy state and route fill. Claims are inspectable without navigation. Approval is explicit and narrow. Reset is always available. Loading, empty, error, reduced-motion, and mobile states are authored in the UI. No operation has an external side effect.

## Responsive behavior

Desktop uses a split case-file/workbench composition. At 1050px, the case file stacks above the workbench. At 650px, the route and ledger remain horizontal where their grammar requires it, while queue and report stack vertically. Preserve legibility over showing every source column at once.

## Avoid

No gradients, glass, glow, chat bubbles, fake metrics, remote imagery, rounded card grids, or hidden confidence theater. The only “magic” is the evidence becoming easier to inspect.
