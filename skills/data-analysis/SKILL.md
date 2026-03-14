---
name: data-analysis
description: This skill should be used when the user asks to "run data analysis", "analyze this dataset", "regress Y on X", "run the main regressions", "produce tables and figures", "end-to-end analysis", "write analysis script", "set up panel regression", "exploratory data analysis", or "produce publication-ready output". Provides end-to-end data analysis workflow for social science research in Python (primary) or Stata, from data loading through publication-ready tables and figures.
version: 1.0.0
---

# Data Analysis Workflow — Social Science Research

End-to-end data analysis: load, explore, analyze, and produce publication-ready output. Primary language is Python (transitioning from Stata); Stata workflows are also supported.

**Input:** Dataset path or description of analysis goal (e.g., "regress log wages on education with individual fixed effects using PSID panel 2000-2020").

---

## Constraints

- Use relative paths everywhere — no hardcoded absolute paths
- Set seed once at top for all stochastic operations
- Save all scripts to `scripts/` with descriptive names
- Save all outputs (figures, tables, processed data) to `output/`
- Follow `coding-style.md` for Python file structure

---

## Workflow Phases

### Phase 1: Setup

**Python setup:**
```python
# ============================================================
# [Descriptive Title]
# Purpose: [What this script does]
# Inputs:  [Data files]
# Outputs: [Figures, tables, parquet/pickle files]
# ============================================================

import random
import numpy as np
import pandas as pd
from pathlib import Path

# Set seed
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Paths
ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUTPUT = ROOT / "output"
(OUTPUT / "figures").mkdir(parents=True, exist_ok=True)
(OUTPUT / "tables").mkdir(parents=True, exist_ok=True)
```

**Stata setup:**
```stata
clear all
set more off
set seed 42

global root  "/path/to/project"  // SET THIS
global data  "$root/data"
global out   "$root/output"
```

### Phase 2: Exploratory Data Analysis

Generate diagnostic outputs before running regressions:

- Summary statistics: means, SDs, min/max, missingness
- Distributions: histograms for key variables
- Time trends: if panel data, plot key variables over time
- Treatment/control balance: compare groups before treatment
- Correlation: between outcome and main predictors

Save all EDA figures to `output/figures/eda/`.

### Phase 3: Main Analysis

**Python — panel regression (linearmodels / pyfixest):**

```python
# Fixed effects regression with clustered SE
from pyfixest.estimation import feols

# Baseline
m1 = feols("log_wage ~ educ | ind_id + year", data=df, vcov={"CRV1": "state"})

# With controls
m2 = feols("log_wage ~ educ + exp + exp2 | ind_id + year", data=df, vcov={"CRV1": "state"})

print(m1.summary())
print(m2.summary())
```

**Python — DID with staggered adoption (pyfixest):**

```python
from pyfixest.estimation import feols
from pyfixest.report import etable

# Two-way FE (baseline, biased under staggered)
twfe = feols("y ~ i(rel_time, ref=-1) | unit + year", data=df, vcov={"CRV1": "unit"})

# Sun & Abraham (2021) heterogeneity-robust
sa = feols("y ~ sunab(cohort, rel_time) | unit + year", data=df, vcov={"CRV1": "unit"})
```

**Stata — equivalent:**
```stata
reghdfe log_wage educ, absorb(ind_id year) cluster(state)
estimates store m1

reghdfe log_wage educ exp c.exp#c.exp, absorb(ind_id year) cluster(state)
estimates store m2
```

### Phase 4: Publication-Ready Output

**Regression tables — Python:**

```python
from pyfixest.report import etable

# Export to LaTeX
etable([m1, m2, m3],
       file="output/tables/table1.tex",
       digits=3,
       coef_fmt="b (se)")
```

**Figures — Python (ggplot-style with plotnine):**

```python
from plotnine import ggplot, aes, geom_point, geom_line, theme_bw, labs, ggsave

fig = (ggplot(df_plot, aes(x="year", y="estimate", ymin="ci_low", ymax="ci_high"))
       + geom_point()
       + geom_line()
       + theme_bw()
       + labs(x="Year", y="Coefficient Estimate", title="Event Study"))

ggsave(fig, "output/figures/event_study.pdf", width=7, height=5)
ggsave(fig, "output/figures/event_study.png", width=7, height=5, dpi=300)
```

**Save objects for reuse:**

```python
import pickle

with open("output/reg_results.pkl", "wb") as f:
    pickle.dump({"m1": m1, "m2": m2}, f)
```

### Phase 5: Quality Check

Before finalizing:

1. Verify script runs top-to-bottom without errors
2. Check: Are SEs clustered at the right level? Justify in a comment.
3. Check: Is the effect size economically meaningful? Add a sentence.
4. Check: Are all output files labeled and self-contained?
5. Apply quality-gates scoring (target ≥ 80)

---

## Common Analysis Patterns

### Event Study / DID Pre-Trends

```python
# Plot coefficients from dynamic DID
twfe_coefs = twfe.coef().reset_index()
twfe_coefs["t"] = twfe_coefs["Coefficient"].str.extract(r"rel_time::(-?\d+)").astype(float)
# Plot with CI bands — see Phase 4 for plotnine code
```

### IV / 2SLS

```python
from pyfixest.estimation import feols

# First stage + IV
iv = feols("y ~ x2 | id + year | x1 ~ z1", data=df, vcov={"CRV1": "state"})
print(iv.first_stage())  # F-statistic
```

### RDD

```python
from rdrobust import rdrobust, rdplot

rdd = rdrobust(y=df["outcome"], x=df["running"], c=0)
rdplot(y=df["outcome"], x=df["running"], c=0)
```

---

## Stata-to-Python Translation Reference

| Stata | Python (pyfixest/linearmodels) | Notes |
|-------|-------------------------------|-------|
| `reghdfe y x, absorb(id year) cluster(g)` | `feols("y ~ x \| id + year", vcov={"CRV1": "g"})` | Check if df-adjustment differs |
| `areg y x, absorb(id) cluster(g)` | `feols("y ~ x \| id", vcov={"CRV1": "g"})` | Equivalent |
| `ivreg2 y (x=z), cluster(g)` | `feols("y ~ 1 \| id \| x ~ z", vcov={"CRV1": "g"})` | First stage F-stat: `iv.first_stage()` |
| `bootstrap, reps(999): reg y x` | `resample + loop` | Match seed, reps, bootstrap type |
| `estout m1 m2 using t.tex` | `etable([m1, m2], file="t.tex")` | pyfixest ≥ 0.18 |

---

## Important

- **Reproduce, don't guess.** If the user specifies a regression, run exactly that specification.
- **Show your work.** Print summary statistics before jumping to regressions.
- **Check for issues.** Look for multicollinearity, outliers, treatment overlap.
- **Comment identification logic.** Each regression should have a 1-2 line comment explaining what variation is being exploited and what threat is being addressed.
