# Orchestrator Protocol: Contractor Mode

After a plan is approved, enter contractor mode and execute autonomously.

## The Loop

```
Plan approved → orchestrator activates
  │
  Step 1: IMPLEMENT — Execute plan steps in order
  │
  Step 2: VERIFY — Run code / compile LaTeX / check outputs
  │         If verification fails → fix → re-verify (max 2 retries)
  │
  Step 3: REVIEW — Apply adversarial QA (for papers/analysis)
  │         Critic agent: find problems
  │         Fixer agent: implement corrections
  │         Loop until APPROVED or 5 rounds max
  │
  Step 4: SCORE — Apply quality-gates rubric
  │
  └── Score >= 80?
        YES → Present summary to user
        NO  → Loop back to Step 3 (max 5 rounds)
              After max rounds → present with remaining issues listed
```

## Adversarial QA (Paper Writing)

When working on any paper section or full manuscript:

1. **Critic agent** — acts as a hostile referee at AER/APSR:
   - Attack identification strategy: "What's the key threat to validity here?"
   - Challenge economic magnitude: "Is this effect size meaningful?"
   - Find missing citations: "What prior work does this contradict?"
   - Detect AI writing patterns: "What sounds unnatural or formulaic?"

2. **Fixer agent** — addresses each critique:
   - Revise prose, add robustness, clarify assumptions
   - Mark remaining issues as acknowledged limitations

3. Loop until no critical issues remain (max 5 rounds)

## Adversarial QA (Data Analysis)

When reviewing regression output or analysis scripts:

1. **Critic agent** — statistical adversary:
   - "Are standard errors appropriate for this design?"
   - "Is there a pre-trends test?"
   - "Could this result be driven by outliers?"

2. **Fixer agent** — adds robustness checks, alternative specs

## "Just Do It" Mode

When user says "just do it" / "go ahead" / "handle it":
- Skip mid-task approval pauses
- Still run the full verify-review-fix loop
- Present summary at end with quality score

## Limits

- Main loop: max 5 review-fix rounds
- Critic-fixer sub-loop: max 5 rounds
- Verification retries: max 2
- Never loop indefinitely

## Requirements Specification (Complex Tasks)

For ambiguous or large tasks (>3 files or >1 hour):
1. Use AskUserQuestion (max 3-5 questions) to clarify MUST/SHOULD/MAY
2. State CLEAR / ASSUMED / BLOCKED for each major aspect
3. Get approval on spec before planning
4. THEN draft and execute plan

Reduces mid-plan pivots by ~40%.
