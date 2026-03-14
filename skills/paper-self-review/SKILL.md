---
name: paper-self-review
description: This skill should be used when the user asks to "review paper quality", "self-review before submission", "check paper completeness", "score my paper", "validate paper structure", "check identification strategy", "pre-submission review", or "run quality check on paper". Provides systematic 0-100 scored review for economics and political science papers before advisor review or journal submission.
version: 2.0.0
---

# Paper Self-Review — Scored Quality Audit

Systematic 0-100 scored review for social science papers. Produces a structured report with blocking issues, warnings, and a submission readiness verdict.

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 90+ | Journal submission | Ready to submit |
| 85+ | Advisor/coauthor review | Ready to share |
| 80+ | Draft commit | Good enough to save |
| < 80 | Not ready | Fix blocking issues first |

---

## Step 1: Locate and Read the Paper

Read the full paper (`.tex`, `.pdf`, or `.qmd`). For long papers, read in logical chunks:
- Abstract + Introduction
- Theory/Hypotheses (if present)
- Data + Empirical Strategy
- Results + Robustness
- Conclusion

---

## Step 2: Score Across 8 Dimensions

Start at 100. Apply deductions for each issue found.

### Dimension 1: Identification & Causal Credibility (max deduction: 40)

| Issue | Deduction |
|-------|-----------|
| Key identifying assumption not stated explicitly | -15 |
| Main threat to validity not acknowledged | -10 |
| No robustness checks / sensitivity analysis | -10 |
| Pre-trends / placebo tests missing (for DID/RDD) | -8 |
| Clustered SE not justified | -5 |
| Multiple testing not addressed | -5 |

### Dimension 2: Main Results (max deduction: 25)

| Issue | Deduction |
|-------|-----------|
| Primary estimate missing or wrong sign | -20 |
| No economic magnitude interpretation | -8 |
| Effect size not benchmarked to existing literature | -5 |
| Significance without magnitude discussion | -5 |
| Tables not self-contained (missing notes) | -5 |

### Dimension 3: Introduction Quality (max deduction: 20)

| Issue | Deduction |
|-------|-----------|
| Research question not stated in first 2 paragraphs | -10 |
| Contribution not differentiated from prior work | -8 |
| Main finding with magnitude not in introduction | -8 |
| Identification strategy not summarized | -5 |
| No roadmap | -3 |

### Dimension 4: Theory / Hypotheses (max deduction: 15, PolSci only)

| Issue | Deduction |
|-------|-----------|
| Hypotheses not numbered and explicit (APSR/JOP) | -10 |
| Causal mechanism not specified | -8 |
| Theory disconnected from empirics | -8 |

### Dimension 5: Data & Measurement (max deduction: 15)

| Issue | Deduction |
|-------|-----------|
| Key variable operationalization unexplained | -8 |
| Sample selection not justified | -5 |
| Descriptive statistics missing | -5 |
| Data source not cited with access info | -3 |

### Dimension 6: Literature Positioning (max deduction: 15)

| Issue | Deduction |
|-------|-----------|
| Missing seminal paper in this literature | -10 |
| Contribution not clearly differentiated | -8 |
| Prior findings mischaracterized | -8 |
| Broken citation (\cite{} undefined) | -5 per |

### Dimension 7: Writing Quality (max deduction: 10)

| Issue | Deduction |
|-------|-----------|
| AI writing patterns (hollow hedges, filler phrases) | -5 |
| Abstract missing key result with magnitude | -5 |
| Passive voice where active would be clearer | -2 |
| Notation inconsistency within paper | -3 |

### Dimension 8: Presentation (max deduction: 10)

| Issue | Deduction |
|-------|-----------|
| Figure axis labels missing | -3 per |
| Table lacks column headers or notes | -3 per |
| Compilation error (LaTeX) | -10 |
| Overfull hbox > 10pt | -2 |

---

## Step 3: Generate Referee Objections

Produce 3-5 specific questions a hostile referee at a top journal would raise:

- Attack the identification strategy directly
- Challenge economic/political significance of the magnitude
- Point to missing heterogeneity analysis
- Flag inconsistency between theory and empirics
- Identify gaps in the literature review

---

## Step 4: Output Format

```markdown
# Paper Self-Review: [Paper Title]

**Date:** YYYY-MM-DD
**Track:** [Economics / Political Science]
**Target journal:** [If known]

---

## Overall Score: [N]/100

**Submission Readiness:** [READY / REVISE / NOT READY]

---

## Score Breakdown

| Dimension | Deductions | Subtotal |
|-----------|-----------|---------|
| 1. Identification & Causality | -X | Y/100 |
| 2. Main Results | -X | Y/100 |
| 3. Introduction | -X | Y/100 |
| 4. Theory/Hypotheses | -X | Y/100 |
| 5. Data & Measurement | -X | Y/100 |
| 6. Literature | -X | Y/100 |
| 7. Writing Quality | -X | Y/100 |
| 8. Presentation | -X | Y/100 |
| **TOTAL** | | **[N]/100** |

---

## Blocking Issues (must fix before submission)

### B1: [Title]
- **Dimension:** [Which dimension]
- **Issue:** [Specific description with location]
- **Fix:** [Concrete action required]

[Repeat for all blocking issues]

---

## Warnings (should fix)

### W1: [Title]
- **Issue:** [Description]
- **Suggested fix:** [Action]

---

## Referee Objections

### RO1: [Objection]
**Why fatal:** [Why this could cause rejection]
**How to address:** [Response or additional analysis]

[Repeat for 3-5 objections]

---

## Strengths

1. [What works well]
2. [What works well]

---

## Summary

[2-3 sentences: overall assessment and priority actions]
```

---

## Principles

- Score 0-100 strictly — no inflation
- Every critique must include a concrete fix
- Distinguish blocking (< 80 without fixing) from warnings
- Think like a hostile referee at a top-5 journal
- Save report to session log under `## Paper Review`
