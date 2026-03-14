---
name: results-analysis
description: This skill should be used when the user asks to "analyze empirical results", "generate results section", "interpret regression output", "create regression tables", "visualize DID results", "plot event study", "check pre-trends", "first stage F-statistic", "run robustness checks", "interpret causal estimates", or mentions connecting empirical analysis to social science paper writing. Covers DID, IV, RDD, and Synthetic Control designs.
tags: [Research, CausalInference, Statistics, Visualization, Econometrics]
version: 1.0.0
---

# Results Analysis for Social Science Empirical Research

A systematic empirical results analysis workflow for political science and economics papers — from raw regression output to publication-ready tables, figures, and Results section text.

## Core Features

1. **Identification Assumption Checks** — Pre-trend tests, first-stage F, McCrary density, MSPE ratios
2. **Main Results Presentation** — Regression tables with proper SE clustering, LaTeX output
3. **Robustness Battery** — Alternative specifications, placebo tests, subgroup analysis
4. **Visualization** — Event study plots, coefficient plots, RD plots, binned scatter
5. **Results Section Writing** — Social science journal structure (APSR/AJPS/AER/QJE)

## When to Use

- Validate identification assumptions (pre-trends, exclusion restriction, continuity)
- Generate LaTeX regression tables ready for insertion
- Create event study / coefficient plots
- Conduct and report robustness checks
- Write or revise the Results / Empirical Findings section
- Interpret causal estimates in substantive terms

---

## Workflow

```
Data Loading → Identification Checks → Main Results → Robustness → Visualization → Writing → Quality Check
```

### Step 1: Data and Output Loading

**Common Input Formats:**
- `.dta` — Stata dataset (load via `pystata` or `pandas` + `pyreadstat`)
- `.csv` — Panel / cross-sectional data
- Stata log (`.smcl` / `.log`) — Regression output to parse
- Python objects — Results from `statsmodels`, `linearmodels`, `econml`

**Initial Data Checks:**
- Sample dimensions: N units, T periods, total observations
- Panel structure: balanced vs. unbalanced, attrition pattern
- Missing values: which variables, which groups/periods
- Treatment/control proportions and overlap

---

### Step 2: Identification Assumption Checks

**Always validate before reporting main results.**

#### DID / Event Study
- **Pre-trend test**: plot event-study coefficients for periods t = −k to t = −1; all should be statistically indistinguishable from zero
- **Parallel trends visual**: plot raw outcome trends for treated and control groups pre-treatment
- **Anticipation effects**: inspect t = −1 and t = −2 coefficients
- **Callaway-Sant'Anna / Sun-Abraham** for staggered treatment: check for heterogeneity-robust estimates

#### Instrumental Variables
- **First stage F-statistic**: report Kleibergen-Paap (clustered) F, not Cragg-Donald; Stock-Yogo critical values
- **Weak instrument**: F > 10 as rule of thumb; F > 104.7 for 5% size distortion (Stock-Yogo)
- **Exclusion restriction**: theoretical argument + placebo outcome test
- **Endogeneity test**: Hausman test (if OLS and IV differ significantly, report both)

#### RDD
- **Density continuity**: McCrary (2008) test; plot histogram around cutoff
- **Covariate balance**: run RDD on pre-determined covariates (should be ≈ 0)
- **Optimal bandwidth**: IK (2012) or CCT (2014); report results across multiple bandwidths
- **Donut-hole robustness**: exclude observations very close to cutoff

#### Synthetic Control
- **Pre-period fit**: MSPE ratio (treated vs. donor pool); target < 2
- **Placebo in-space**: run SC for each donor unit; treated effect should be an outlier
- **Placebo in-time**: use an artificial earlier treatment date; effect should be near zero
- **Leave-one-out**: drop each donor and re-run; check stability

See `references/identification-checklist.md` for detailed protocols and code snippets.

---

### Step 3: Main Results

**Regression Table Standards (social science journals):**

| Element | Requirement |
|---------|-------------|
| Standard errors | Clustered at appropriate level (state, county, individual); heteroskedasticity-robust as minimum |
| Significance markers | †p<0.10, *p<0.05, **p<0.01, ***p<0.001 (or journal-specific) |
| Fixed effects rows | Include "Unit FE ✓", "Time FE ✓" rows at bottom |
| Sample info | N (observations), N_clusters if clustered |
| Model fit | R² (within R² for FE models), first-stage F for IV |

**Recommended Column Progression:**
```
(1) OLS / Baseline
(2) Main specification (DID / IV / RDD)
(3) + Controls
(4) Alternative clustering
(5) Alternative fixed effects / specification
```

**Effect Size Interpretation:**
- Raw coefficient + percentage of outcome mean (e.g., "0.23 SD increase, or 14% of the sample mean")
- For log outcomes: elasticity ("a 10% increase in X → Y% change in outcome")
- For binary outcomes: marginal effects at the mean alongside LPM/logit

---

### Step 4: Robustness Checks

**Standard Robustness Battery:**

| Check | Description |
|-------|-------------|
| Alternative window/bandwidth | ±50%, ±200% of main specification |
| Different control sets | No controls → parsimonious → saturated |
| Alternative outcome definitions | Different measurement, normalization |
| Alternative clustering level | One level up / down |
| Wild bootstrap | For small N_cluster (< 50) |
| Placebo treatment | Assign treatment to untreated units |
| Placebo outcome | Test on predetermined variable |
| Subgroup analysis | Key heterogeneity dimensions |
| Balanced panel | Restrict to always-observed units |

Present robustness as a **coefficient plot** across specifications (point estimate + 95% CI per column), or a robustness table in the appendix.

---

### Step 5: Visualization

**Event Study / Coefficient Plot:**
- Point estimates + 95% CI for each event-time period
- Reference line at zero; vertical dashed line at treatment date
- Pre-period serves as visual identification test
- Use `matplotlib` + `pandas` or `plotnine` (ggplot2 equivalent)

**Coefficient Plot (across specifications):**
- One row per specification, all on same scale
- Ordered by model complexity or specification dimension

**RD Plot:**
- Binned scatter with local polynomial fit on each side of cutoff
- Confidence band around polynomial
- Raw scatter as background (lighter color)

**Binned Scatter:**
- For non-parametric relationship visualization
- Residualize on controls / FE before binning

**Publication Standards:**
- Vector format (PDF preferred for journals)
- Colorblind-safe palette (Okabe-Ito or similar)
- Font size ≥ 10pt
- Axis labels in plain English (not variable names like `ln_gdppc`)
- Caption must be self-contained

See `references/visualization-guide.md` for Python/Stata code templates.

---

### Step 6: Writing the Empirical Results Section

**Social Science Results Structure:**

```markdown
## [N]. Empirical Results

### [N.1] Main Results
[Lead with headline number and substantive significance]
[Table X presents the main results. Column (1) shows... Column (2) adds...]
[Interpret magnitude: "a one-standard-deviation increase in X is associated with a Y-unit / Z% change in outcome"]

### [N.2] Identification Tests
[Pre-trend test: "Figure X plots event-study coefficients... none of the pre-treatment coefficients are statistically distinguishable from zero"]
[First stage: "The Kleibergen-Paap F-statistic is XX, exceeding the Stock-Yogo critical value"]

### [N.3] Robustness
[Brief summary: "These results are robust to..."; point to Appendix Table X]

### [N.4] Heterogeneity / Mechanisms
[Which subgroups show larger/smaller effects and why — connect to theory]
```

**Writing Principles:**
- Lead with **substantive significance** ("equivalent to 0.3 years of average wage growth"), not just stars
- Always interpret magnitudes in context
- Explicitly link identification evidence back to the causal claim
- Acknowledge limitations honestly; reviewers will raise them anyway

See `references/results-writing-guide.md` for journal-specific style guidance.

---

### Step 7: Quality Checklist

- [ ] Identification assumptions explicitly tested and reported
- [ ] Standard errors clustered at correct level (justified in text)
- [ ] Regression table includes N, FE indicators, clustering info
- [ ] Effect sizes interpreted in substantive terms (not just "significant")
- [ ] Pre-trend / first-stage F / density test results reported
- [ ] At least 3 robustness specifications
- [ ] Figures are vector format, colorblind-safe, self-contained captions
- [ ] Results section connects back to theoretical motivation

---

## Integration with Paper Writing

```
Causal analysis complete (Stata / Python)
    ↓
results-analysis: validate assumptions, generate tables/figures
    ↓
ml-paper-writing: integrate into full paper structure
    ↓
Complete Empirical Results section
```

**This skill handles:**
- Assumption validation and reporting
- Regression tables (LaTeX)
- Visualization (event study, coefficient plots, RD plots)
- Results section drafting

**ml-paper-writing handles:**
- Full paper structure (Introduction, Theory, Data, Conclusion)
- Citation formatting
- Journal submission requirements

---

## Reference Resources

- **`references/identification-checklist.md`** — DID/IV/RDD/SC assumption testing with code
- **`references/visualization-guide.md`** — Python + Stata code templates for coefficient plots, event studies
- **`references/results-writing-guide.md`** — Results section writing standards for APSR/AJPS/AER/QJE
- **`references/statistical-methods.md`** — Statistical tests reference (clustered SE, wild bootstrap, etc.)
