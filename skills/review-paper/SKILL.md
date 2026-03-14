---
name: review-paper
description: This skill should be used when the user asks to "review this paper", "give referee report", "simulate peer review", "what would a referee say", "critique this manuscript", "review paper for AER/APSR", "manuscript review", or "find weaknesses in this paper". Produces a detailed structured referee report covering identification, econometrics, literature, and writing — the kind a top-5 journal referee would write.
version: 1.0.0
---

# Manuscript Review — Referee Report

Produce a thorough, constructive review of an academic manuscript. Think like a demanding but fair referee at AER, QJE, APSR, or AJPS.

**Input:** Path to paper (`.tex`, `.pdf`, `.qmd`), or paper title in context.

---

## Steps

### 1. Locate and Read

Read the full paper end-to-end. For long papers, read in chunks:
- Abstract + Introduction (always first)
- Theory/hypotheses
- Data + identification strategy
- Results + robustness
- Conclusion

### 2. Evaluate Across 6 Dimensions

#### Dimension 1: Argument Structure
- Is the research question clearly stated in the introduction?
- Does the logical flow hold: question → design → results → conclusion?
- Are the conclusions supported by the evidence presented?
- Are limitations acknowledged honestly?

#### Dimension 2: Identification & Causal Credibility
- What is the causal claim? Is it credible?
- Are the key identifying assumptions stated explicitly?
- What are the main threats to identification (omitted variables, reverse causality, attrition)?
- Are robustness checks adequate and appropriate?
- Are pre-trends tests shown (for DID)? Fuzzy first-stage (for RDD/IV)?
- Is the estimator appropriate for the research design?

#### Dimension 3: Econometric Specification
- Are standard errors appropriate (clustered, heteroskedasticity-robust, bootstrap)?
- Is the functional form justified?
- Are effect sizes economically meaningful — not just statistically significant?
- Are there multiple testing concerns?
- Is the regression table complete (N, R-squared, fixed effects notation)?

#### Dimension 4: Literature Positioning
- Are seminal papers in this literature cited?
- Is prior work characterized accurately?
- Is the contribution clearly differentiated from existing work?
- Are there obvious missing citations a referee would flag?

#### Dimension 5: Writing Quality
- Is the abstract specific — does it state the main result with magnitude?
- Is the introduction self-contained (contribution clear without reading the whole paper)?
- Is notation consistent throughout?
- Are tables and figures self-contained (clear labels, units, source notes)?

#### Dimension 6: Data and Measurement
- Is the main outcome variable credibly operationalized?
- Is sample selection (inclusion/exclusion criteria) justified?
- Are descriptive statistics presented?
- Are data sources cited with access information?

### 3. Generate Referee Objections

Produce 3-5 specific fatal objections a hostile referee would raise:
- Attack the identification strategy first (this is where papers die)
- Challenge the economic/political significance of the effect size
- Identify the most glaring gap in the literature review
- Point to a missing heterogeneity analysis that would reveal mechanism
- Flag any inconsistency between the theory and the empirics

---

## Output Format

```markdown
# Referee Report: [Paper Title]

**Date:** YYYY-MM-DD
**Reviewer:** review-paper skill
**Track:** [Economics / Political Science]
**Recommendation:** [Strong Accept / Accept / Minor R&R / Major R&R / Reject]

---

## Summary Assessment

[2-3 paragraphs: main contribution, key strengths, fatal concerns]

---

## Major Concerns

### MC1: [Short Title]
- **Dimension:** [Identification / Econometrics / Literature / Writing / Data]
- **Issue:** [Specific description with section/table reference]
- **Why it matters:** [How this threatens the paper]
- **Suggested fix:** [Concrete action]

[Repeat for each major concern]

---

## Minor Concerns

### mc1: [Title]
- **Issue:** [Description]
- **Fix:** [Action]

---

## Referee Objections (Top 3-5)

### RO1: [The Objection]
**Why this could cause rejection:** [Mechanism]
**How to address:** [Response strategy or additional analysis needed]

---

## Specific Comments

[Section-by-section or line-level comments if needed]

---

## Summary Scorecard

| Dimension | Rating (1-5) | Notes |
|-----------|-------------|-------|
| Argument Structure | [N] | |
| Identification | [N] | |
| Econometrics | [N] | |
| Literature | [N] | |
| Writing | [N] | |
| Data & Measurement | [N] | |
| **Overall** | **[N]** | |
```

---

## Principles

- Every criticism must include a concrete suggested fix
- Reference exact sections, equations, tables — not vague descriptions
- Distinguish fatal flaws (would reject) from addressable concerns (R&R)
- Acknowledge what's done well — good research deserves recognition
- Do NOT fabricate details or citations — flag uncertainty explicitly
- Save the report to the session log or `/plan` folder
