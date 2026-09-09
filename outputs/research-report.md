# Agents for Humans: evidence-bounded build research

Checked September 8, 2026. This report separates published facts, direct observations, and design inferences. Social posts and indexed competitor pages were used as leads, not as authoritative competition rules.

## Decision

Build Tallyline: an evidence-first post-award grant reporting/closeout agent for small nonprofits and community organizations. Its differentiator is a claim ledger that maps each claim to source evidence and keeps unsupported, variance, and consent decisions visible. It prepares a packet; it does not submit, move money, email, or invent impact.

## Competition facts

The official [Agents for Humans Devpost page](https://agentsforhumans.devpost.com/) lists the deadline as September 14, 2026 at 5:00 PM PDT, three tracks, a $40,000 prize pool, required use of a new AI agent built with the Strands Agents SDK, and the Stage 1 / Stage 2 judging flow. Stage 2 is weighted equally across Technical Implementation, Design, Potential Impact, Creativity/Originality, and Presentation. The same page states that teams should provide a public repository with code/assets/setup, a README, an architecture diagram, a permissive license, and a public demo of no more than five minutes. Its judge list includes AWS applied-science, developer-advocacy, partner-architecture, GTM, open-source program, TPM, and software-engineering roles.

The official page is the authority for rules and criteria. Its gallery was not published at research time, so the competition scan could not treat a complete project gallery as available evidence.

## Domain evidence

- [Grants.gov grant reporting](https://www.grants.gov/learn-grants/grant-reporting) describes recipient reporting across financial, compliance, and project/impact information. That supports a workflow that joins more than narrative prose.
- [EPA guidance on outputs and outcomes](https://www.epa.gov/p2/guidance-grantees-reporting-outputs-and-outcomes) distinguishes outputs that are comparatively straightforward to report from outcomes that require more time and attention. Tallyline therefore exposes output reconciliation and does not turn output counts into unsupported impact claims.
- [IRS reports from grantees](https://www.irs.gov/charities-non-profits/private-foundations/reports-from-grantees) explains that reports can cover use of funds, compliance, and progress toward purposes, and that foundations need adequate grantee information. This supports a finance variance queue and evidence index.
- [Grants.gov Data Standards](https://www.grants.gov/data-standards) frames common data standards as a way to reduce recipient burden and improve quality/interoperability. The product's normalized claim ledger is an intentionally small, local expression of that idea, not a claim to implement Grants.gov standards.

## Technical fit

The [Strands Python quickstart](https://strandsagents.com/docs/user-guide/quickstart/python/) documents the `strands-agents` package, `Agent`, and `@tool` flow. Strands' [multi-agent documentation](https://strandsagents.com/docs/user-guide/concepts/multi-agent-systems/) describes agents-as-tools and Graph/Swarm/Workflow patterns. The build uses a bounded coordinator seam and typed tools while keeping deterministic reconciliation in ordinary Python, which makes the local behavior directly inspectable. A live `GeminiModel` probe through the same Strands coordinator completed with both tools invoked; the recorded demo includes that advisory readout. The repository also retains a provider-configured Bedrock path.

The [AWS Bedrock AgentCore runtime guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) describes a framework-agnostic runtime for agents, including Strands, with session and long-running operation support. The Strands [cloud deployment lesson](https://strandsagents.com/docs/learning/deploying-agents-to-the-cloud/) provides the relevant deployment path. This repository does not claim that a live Bedrock/AgentCore deployment, AWS credentialed invocation, or hosted endpoint was completed; those require a separate deployment and live probe.

## Competitive scan and differentiation

Indexed competition examples included QuietRelay, which centered on local Strands-based foodbank stock/volunteer allocation; generic operations agents for post-purchase work; app-operations agents monitoring reviews/revenue/crashes; and security/governance agents. Grant-adjacent products included pre-award discovery/drafting and broader grant lifecycle/compliance platforms. These observations led to explicit exclusions: no food inventory matching, no generic “AI grant writer,” and no irreversible business operations.

The relevant inference is that a closeout-specific claim ledger can be recognizable in a short demo: the operator can see a duplicate row removed, a budget variance held, and a beneficiary note blocked by consent. That is a product-mechanism inference, not a claim that no competitor has any similar capability.

## Judge-lens inferences

The role mix and rubric suggest five useful proof obligations: measurable deterministic behavior for applied-science/SDE review; runnable explanation and setup for DevRel/technical-content review; credible AWS boundaries and user value for partner/GTM review; reproducibility, license, and governance for open-source/TPM review; and a visible, memorable mechanism for the creative/presentation score. These are inferences from public roles and rubric, not private judge guidance.

## X-native signal scan

The account-specific X scan used the available authenticated headless workflow without exposing session material or performing any social actions. Official AWS/Devpost posts confirmed live hackathon promotion, the three-track/$40k framing, and the recurring language around agents handling repetitive paperwork/scheduling. Strands-related chatter showed interest in multi-agent and AgentCore evaluation. Searches for foodbank and Good Neighbor examples did not supply stronger evidence than the indexed project scan. Individual judge searches surfaced public professional content, but not reliable scoring preferences. These are discovery signals only; the official Devpost page remains the source of truth.

## Submission-state verification

1. The local MP4 is recorded, H.264/AAC decoded successfully, 3:47 long at 1440×900, and includes a live Gemini/Strands readout. It is published at [Vimeo](https://vimeo.com/1225124530), and the public watch page was verified.
2. The public repository, license, setup, fixtures, tests, and diagram were verified; the live-model/docs changes are pushed to `main`.
3. If pursuing AWS hosting, deploy with least-privilege tool permissions, verify the live endpoint and logs, and update claims only after the probe succeeds.
4. Add AWS Builder ID and any optional builder.aws post only after they are actually complete.
