---
paths:
  - "**/*.tex"
  - "**/*.do"
  - "**/*.py"
  - "**/*.R"
  - "**/*.qmd"
  - "papers/**"
  - "analysis/**"
---

# Quality Gates & Scoring Rubrics

## Thresholds

| Score | Gate | Action |
|-------|------|--------|
| 80+ | Commit | Good enough to save |
| 85+ | Submission | Ready for advisor / co-author |
| 90+ | Journal | Ready for submission |
| 95+ | Excellence | Aspirational |

Score < 80 → Block commit. List blocking issues explicitly.
Score 80-89 → Allow commit with warning. List recommendations.
User can override with written justification.

---

## Academic Paper Scoring (.tex / .qmd)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Identification assumption not stated | -25 |
| Critical | Main result not present or wrong sign | -20 |
| Critical | Broken citation (undefined \cite{}) | -15 |
| Critical | Compilation failure | -100 |
| Major | No robustness checks | -10 |
| Major | Standard errors not justified | -10 |
| Major | Abstract missing key result with magnitude | -8 |
| Major | Notation inconsistency | -5 |
| Major | Table/figure without notes | -5 |
| Minor | Informal language (AI patterns) | -3 |
| Minor | Missing p-value or CI reporting | -3 |
| Minor | Overfull hbox > 5pt | -2 |

## Stata/Python Analysis Scripts (.do / .py / .R)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Script errors on run | -100 |
| Critical | Hardcoded absolute paths | -20 |
| Critical | No seed for stochastic operations | -15 |
| Major | No comments explaining identification | -10 |
| Major | Missing clustered SE justification | -8 |
| Major | Output files not labeled with date/version | -5 |
| Minor | No log file | -3 |
| Minor | print() instead of logging | -2 |

---

## Tolerance Thresholds (Causal Inference)

| Quantity | Tolerance | Rationale |
|----------|-----------|-----------|
| Point estimates | < 0.01 | Rounding in paper display |
| Standard errors | < 0.05 | Bootstrap/clustering variation |
| P-values | Same significance level | Exact p may differ |
| Coverage rates | ±0.01 | Monte Carlo variability |

---

## Enforcement Protocol

1. Compute score at end of each writing/analysis session
2. Score < 80 → identify blocking issues before stopping
3. On `/commit`: auto-check score; block if < 80 unless overridden
4. Save quality scores in session log under `## Quality Score`
