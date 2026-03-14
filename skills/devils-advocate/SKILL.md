---
name: devils-advocate
description: This skill should be used when the user asks to "play devil's advocate", "challenge my identification", "what are the weaknesses in my paper", "adversarial critique", "stress test my argument", "find holes in my research design", "what would a hostile referee say", or "challenge my empirical strategy". Produces 5-7 specific adversarial challenges targeting the identification strategy, theoretical mechanism, and empirical design of a research project.
version: 1.0.0
---

# Devil's Advocate — Adversarial Research Challenge

Critically challenge a research project or paper with 5-7 specific adversarial questions. The goal is to find the fatal flaws before referees do.

**Philosophy:** "We arrive at the best possible research through active adversarial dialogue. A challenge is a gift — it identifies what needs to be fixed or pre-empted."

---

## Setup

1. Read the paper, proposal, or research description
2. Read any related context (prior drafts, notes, related papers)
3. Adopt the perspective of a hostile referee at the target journal

---

## Challenge Categories

Generate 5-7 challenges drawn from these categories:

### 1. Identification Challenges
> "What if [confounder X] drives both the treatment and the outcome?"
> "The variation you're exploiting could reflect [alternative mechanism] — how do you rule this out?"
> "Your treatment is not randomly assigned — selection into [treatment] likely correlates with [outcome determinant]."

### 2. External Validity Challenges
> "Your setting is [country/period/context] — why should we believe this generalizes to [broader population]?"
> "Your sample systematically excludes [group] — does the result hold for them?"

### 3. Mechanism Challenges
> "You claim the mechanism is [X], but the data could equally support [alternative mechanism Y]."
> "Without direct evidence on the mechanism, this is consistent with [5 different stories]."

### 4. Measurement Challenges
> "Your outcome variable [Z] captures [broader concept] — it's contaminated by [noise source]."
> "Treatment is measured with error — which direction would this bias your estimate?"

### 5. Specification Challenges
> "Why this functional form? [Alternative form] would give a different answer."
> "Your standard errors should be clustered at [higher level] — this would widen your CIs substantially."
> "The control set is [too sparse / over-controlled] — [confounder / bad control] should be [included / excluded]."

### 6. Literature Challenges
> "This is essentially [Paper X] applied to a new context — what's the additional theoretical insight?"
> "You claim to find [result] but [Paper Y (year)] found the opposite — why the discrepancy?"

### 7. Magnitude Challenges
> "Your estimate of [effect] is [implausibly large / small] — what's the benchmark?"
> "Is this effect size economically/politically meaningful? Who would change their behavior based on this?"

---

## Output Format

```markdown
# Devil's Advocate: [Paper/Project Title]

**Date:** YYYY-MM-DD
**Target journal:** [If known]

---

## Challenges

### Challenge 1: [Category] — [Short Title]
**Question:** [The specific adversarial question]
**Why it matters:** [How this threatens the paper — what a referee would write]
**Suggested pre-emption:** [How to address this proactively in the paper]
**Severity:** [Fatal / Major / Minor]

[Repeat for 5-7 challenges]

---

## Verdict

**Strengths:** [2-3 things that are solid and hard to attack]
**Fatal vulnerabilities:** [1-2 issues that must be addressed before submission]
**Pre-emptable concerns:** [2-3 issues addressable with robustness checks or footnotes]

---

## Priority Actions

1. [Most urgent fix]
2. [Second priority]
3. [Third priority]
```

---

## Principles

- Be specific: reference exact sections, tables, variables
- Every challenge must include a suggested resolution
- Prioritize by severity: identification > mechanism > measurement > literature
- Distinguish fatal (would reject) from addressable (would request revision)
- If the research design is strong, say so — not everything needs to be challenged
