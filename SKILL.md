---
name: press-conference-revision-evidence-bound
description: Diagnose and revise defensive academic writing while preserving claim ceilings, evidence status, scope conditions, rival explanations, and conceptual hierarchy. Use for a whole-manuscript batch audit or a tightly authorized, tracked-change revision when an academic paper hides its contribution beneath self-defence, repeated caveats, process narration, or unnecessary comparisons; especially when a qualitative, historical, or mixed-method manuscript must become contribution-forward without becoming promotional or overclaimed. Do not use for first drafting, new research, citation repair, evidence admission, grammar-only polishing, or making claims sound stronger than the evidence permits.
---

# Evidence-Bound Press-Conference Revision

Treat a paper as a clear academic presentation of its best supported contribution, not as a work log or a self-audit. Reframe defensiveness; never remove the information that lets readers judge what the evidence supports.

## Non-negotiable distinction

Do not treat a cue word as a verdict. The target is **rhetorical defensiveness**, not scholarly caution.

- Cut, compress, or reframe self-deprecation, anticipatory answers to objections the manuscript has not invited, redundant hedge stacks, process-log narration, and negative judgments broader than the evidence.
- Keep or relocate a real scope condition, source-status distinction, rival explanation, contradiction, negative finding, ethical caveat, or method limitation whenever it changes how the claim must be read.
- When uncertain, retain the wording and register a query. Do not convert possible to certain, report to observation, authorization to delivery, sequence to mechanism, or a bounded case result to a general law.

Read `references/triage-and-regression.md` before classifying candidates. For the Dalian *Urban Geography* manuscript, also read `references/urban-geography-guardrails.md` before any diagnosis or revision.

## Required inputs and authority order

Collect the smallest current set of materials needed for the task:

1. the latest clean manuscript and, for a revision pass, its tracked baseline;
2. the current manuscript lock and any later author-authorized departure from it;
3. current author decisions and unresolved queries;
4. target-journal guidance and any supplied corpus/style calibration;
5. the source principles and prior audit/return records, as context rather than evidence.

Apply this order: manuscript evidence and active author decisions → lock and claim ceiling → verified journal guidance → corpus-level rhetorical calibration → this skill. Do not use a corpus as a phrase bank or let a style preference override a source status.

## Phase 0 — create a contribution-and-scope contract

Before scanning, write a compact contract. Do not edit until it is complete.

| field | required content |
| --- | --- |
| core contribution | One evidence-bound sentence naming the primary analytical move and payoff. |
| contribution hierarchy | Primary concept; supporting lens; bounded empirical contribution; portable payoff, if any. |
| claim ceiling | The strongest permissible formulation already supported by the manuscript and its evidence. |
| load-bearing cautions | Scope, source-status, method, rival, contradiction, and ethics statements that must survive. |
| edit authority | Sections/paragraphs authorized, locked items, tracking requirements, and prohibited changes. |
| live queries | Meaning-dependent choices that must not be silently resolved. |

If the hierarchy, evidence ceiling, or editing authority is unclear, stop after the diagnostic register and request a decision.

## Phase 1 — batch diagnostic (read-only)

Read the whole manuscript once for section roles and the contribution contract. Then make a candidate register; do not revise prose in this phase.

1. Optionally run `scripts/scan_defensive_cues.py` on the clean DOCX to create a **candidate list only**. Inspect every result in context; the script makes no rhetorical or evidentiary decision.
2. Review every prose-bearing paragraph, including title, abstract, introductions, discussion, conclusion, captions, notes, and references only where they affect visible prose.
3. Classify each candidate using the taxonomy in `references/triage-and-regression.md`.
4. Record the candidate in a copy of `assets/defensive-writing-audit-template.csv` or an equivalent table. Include its evidentiary function, source-status tag, contribution relation, and provisional disposition.
5. Mark non-defensive but load-bearing language as `KEEP`; this makes the integrity decision auditable rather than invisible.

Allowed dispositions are `KEEP`, `TIGHTEN`, `REFRAME`, `RELOCATE`, `CUT`, and `QUERY`. A `CUT` must remove rhetoric only, never a factual proposition, citation function, evidence status, rival, or scope limit.

## Phase 2 — concentrated revision (only with authority)

Revise by pattern group and section role, not by a blind word hunt. Use tracked changes when the manuscript is under review.

1. Start with the abstract, introduction, discussion, and conclusion: make the problem, gap, distinctive analytical move, evidence-bound finding, and payoff legible before qualifications appear.
2. In theory and methods, replace self-defence with precise positioning, but keep definitions, scope, evidence-status distinctions, and analytical rivals.
3. In empirical sections, retain contradictions, delay, non-adoption, reversal, and negative findings when they are the data or explain the mechanism. Remove only authorial apology or unnecessary rehearsal of a limitation.
4. Keep a contribution sentence standing in each major section. A later qualifier may narrow it; it may not erase it or turn the paragraph into a response to a hypothetical reviewer.
5. For every changed sentence, run the three-part preservation test: (a) same or narrower claim, (b) same source-status distinction, and (c) same citation/quotation role.
6. Route a change to `QUERY` if it would alter research questions, terminology, hierarchy, evidence, citation role, table/figure text, paragraph order, or a real methodological limitation.

Never solve a mismatch by adding evidence, strengthening a causal verb, or extending a case-specific statement into a general claim.

## Phase 3 — whole-manuscript regression

Read the revised manuscript independently of the change list. Use the regression protocol in `references/triage-and-regression.md`.

Verify all of the following:

- contribution hierarchy is stable from title and abstract through conclusion;
- a new general-first opening is aligned with the body, or the mismatch is explicitly left as a query;
- every changed claim stays within the original evidence ceiling;
- plan, authorization, reported work, observation, outcome, interpretation, and causal inference remain distinct;
- terminology is consistent without flattening meaningful distinctions;
- citations, quotations, dates, numbers, captions, footnotes, figure/table cross-references, and paragraph boundaries remain protected;
- no automatic global replacement has elevated a secondary lens or introduced a prohibited keyword;
- the clean file has accepted changes only and the tracked file exposes every text change.

Use a global terminology scan only to locate candidates. Never replace a concept merely because it is frequent.

## Dalian Urban Geography special gate

When the target is the Dalian heritage-metabolism manuscript, apply the project guardrails before Phase 1 and again before delivery. In particular:

- keep heritage metabolism primary and operation-centred;
- keep rescaling supporting, rival-open, and conditional on a documented capacity-to-operation relation;
- do not promote governance/governing into a master concept or weaken source-specific terms by global substitution;
- preserve overlapping configurations, contradiction, lag, decoupling, reversal, and recombination as analytic findings rather than defensive residue;
- treat the recent general-first abstract/introduction reframe as a cross-section consistency question, not permission to rewrite the body without explicit authority.

## Deliverables and stop rules

For a diagnostic pass, return:

- the contribution-and-scope contract;
- the candidate register with `KEEP` decisions visible;
- a section-level concentration map and an exception/query register;
- a bounded revision recommendation, including which changes require author authority.

For an authorized revision pass, additionally return:

- tracked and clean manuscript copies;
- a change summary organized by pattern group;
- a claim/evidence regression report;
- a list of deliberate non-edits and unresolved author decisions.

Stop after the requested diagnostic or authorized revision pass. Do not submit, conduct new research, change citations, silently resolve a meaning-dependent query, or turn the paper into promotional prose.
