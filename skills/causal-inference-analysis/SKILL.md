---
name: causal-inference-analysis
description: Use when the user asks to "implement DID", "run difference-in-differences", "set up IV regression", "instrumental variables", "run RDD", "regression discontinuity", "synthetic control", "staggered treatment", "Callaway-Sant'Anna", "Sun-Abraham", "event study", "parallel trends test", "first stage", "Bartik instrument", "shift-share IV", "write Stata regression code", "convert Stata to Python", "use statsmodels", "use linearmodels", "use econml", "panel data regression", "fixed effects", "two-way fixed effects", "cluster standard errors", or any causal inference methodology in Python or Stata.
tags: [CausalInference, DID, IV, RDD, SyntheticControl, Python, Stata, Econometrics]
version: 1.0.0
---

# Causal Inference Analysis

Practical implementation guide for DID, IV, RDD, and Synthetic Control in Python and Stata. Covers setup, estimation, assumption testing, and output generation.

## Quick Reference

| Method | Python Library | Stata Command |
|--------|---------------|---------------|
| Two-way FE / DID | `linearmodels.PanelOLS` | `reghdfe` |
| Staggered DID (CS) | `csdid` / `pyfixest` | `csdid` (ado) |
| Staggered DID (SA) | `pyfixest` | `eventstudyinteract` |
| IV / 2SLS | `linearmodels.IV2SLS` | `ivregress 2sls` / `ivreg2` |
| Shift-share IV | manual + `linearmodels` | `ssiv` (ado) |
| RDD | `rdd` / `rdrobust` (Python) | `rdrobust`, `rddensity` |
| Synthetic Control | `synth_runner` / `pysynth` | `synth` |
| Double-LASSO | `doubleml` | `pdslasso` |

---

## Method 1: Difference-in-Differences

### Standard 2×2 DID (Python)

```python
import pandas as pd
from linearmodels import PanelOLS
import statsmodels.formula.api as smf

# Panel setup
df = df.set_index(['unit_id', 'year'])

# Two-way FE (unit + time)
mod = PanelOLS.from_formula(
    'outcome ~ treat_post + EntityEffects + TimeEffects',
    data=df,
    drop_absorbed=True
)
res = mod.fit(cov_type='clustered', cluster_entity=True)
print(res.summary)
```

### Event Study / Dynamic DID (Python)

```python
import pyfixest as pf

# Staggered DID — Sun-Abraham (2021)
fit = pf.feols(
    'outcome ~ i(rel_time, treated, ref=-1) | unit + year',
    data=df,
    vcov={'CRV1': 'state'}  # cluster at state level
)
pf.iplot(fit)  # coefficient plot with 95% CI
```

### Callaway-Sant'Anna (staggered, Python)

```python
from csdid import att_gt, aggte

# Estimate group-time ATTs
att = att_gt(
    yname='outcome',
    tname='year',
    idname='unit_id',
    gname='first_treat',  # 0 for never-treated
    data=df,
    control_group='nevertreated',
    est_method='dr'  # doubly robust
)
agg = aggte(att, type='dynamic')  # event-study aggregation
```

### Pre-trend Test Interpretation

- Coefficients at t = −1, −2, ..., −k should be near zero and statistically insignificant
- Report the joint F-test for pre-period coefficients
- If pre-trends detected: consider controlling for unit-specific linear trends or using CS/SA estimators

---

## Method 2: Instrumental Variables

### Basic 2SLS (Python)

```python
from linearmodels import IV2SLS

mod = IV2SLS.from_formula(
    'outcome ~ 1 + controls [endog ~ instrument]',
    data=df
)
res = mod.fit(cov_type='robust')  # or 'clustered', cluster='state'
print(res.summary)

# Key diagnostics
print(f"First-stage F: {res.first_stage.diagnostics}")
print(f"Wu-Hausman: {res.wu_hausman()}")
```

### Shift-Share (Bartik) IV

```python
# Bartik instrument = Σ_k (local_share_k × national_growth_k)
df['bartik'] = (
    df[share_cols]
    .multiply(national_growth, axis=1)
    .sum(axis=1)
)

# Use as standard IV
mod = IV2SLS.from_formula(
    'outcome ~ controls [endog ~ bartik]',
    data=df
)
```

**Key diagnostics to report:**
- Kleibergen-Paap F (for clustered SE) — not Cragg-Donald
- Stock-Yogo critical values for size distortion
- First-stage coefficient on instrument with SE

---

## Method 3: Regression Discontinuity

### Sharp RDD (Python)

```python
from rdrobust import rdrobust, rdplot, rdbwselect

# Main estimate
result = rdrobust(y=df['outcome'], x=df['running_var'], c=0)
print(result.coef)   # LATE at cutoff
print(result.se)     # SE (conventional, robust, bias-corrected)
print(result.bws)    # Optimal bandwidth (IK/CCT)

# RD plot
rdplot(y=df['outcome'], x=df['running_var'], c=0)

# Density test (McCrary)
from rddensity import rddensity
dens = rddensity(X=df['running_var'], c=0)
print(dens.test)
```

### RDD Robustness Checklist

```python
# 1. Multiple bandwidths
for bw_mult in [0.5, 0.75, 1.0, 1.25, 1.5]:
    bw = optimal_bw * bw_mult
    r = rdrobust(y, x, c=0, h=bw)
    print(f"BW×{bw_mult}: {r.coef[0]:.3f} ({r.se[0]:.3f})")

# 2. Covariate balance (run RDD on predetermined controls)
for cov in ['age', 'income_baseline', 'education']:
    r = rdrobust(y=df[cov], x=df['running_var'], c=0)
    print(f"{cov}: {r.coef[0]:.3f} (p={r.pv[0]:.3f})")

# 3. Donut hole (exclude ±ε of cutoff)
for donut in [0.1, 0.2, 0.5]:
    df_donut = df[abs(df['running_var']) > donut]
    r = rdrobust(y=df_donut['outcome'], x=df_donut['running_var'], c=0)
    print(f"Donut ±{donut}: {r.coef[0]:.3f}")
```

---

## Method 4: Synthetic Control

### Basic Synthetic Control (Python)

```python
# Option 1: pysynth
from pysynth import Synth

synth = Synth()
synth.fit(
    dataprep_dict={
        'foo': 'bar'  # see references/synth-workflow.md for full setup
    }
)
synth.plot(periods_pre_treatment=15, periods_post_treatment=10)
synth.weights()  # donor unit weights

# Option 2: Manual (more transparent)
# See references/synth-manual.md
```

**Placebo tests:**
```python
# In-space: run SC for each donor unit
for donor in donor_pool:
    df_placebo = df[df['unit'] != treated_unit]
    df_placebo['treated'] = (df_placebo['unit'] == donor)
    # Run SC, record post-period MSPE
    # If treated MSPE >> median donor MSPE → significant effect
```

---

## Stata → Python Translation

Common Stata patterns and their Python equivalents:

| Stata | Python |
|-------|--------|
| `reghdfe y x, absorb(unit year) cluster(state)` | `PanelOLS` + `cov_type='clustered'` |
| `ivregress 2sls y x (endog = iv), cluster(state)` | `IV2SLS` with clustered SE |
| `rdrobust y x, c(0) kernel(triangular)` | `rdrobust(y, x, c=0, kernel='triangular')` |
| `estout` / `esttab` | `stargazer` or `modelsummary` (Python) |
| `coefplot` | `pyfixest.iplot()` or manual `matplotlib` |

See `references/stata-to-python.md` for detailed translation guide.

---

## Output Generation

### Regression Table (LaTeX)

```python
import stargazer
from stargazer.stargazer import Stargazer

# statsmodels results
sg = Stargazer([res1, res2, res3])
sg.title('Main Results: Effect of X on Y')
sg.custom_columns(['OLS', 'DID', 'DID + Controls'], [1, 1, 1])
sg.covariate_order(['treat_post', 'control1', 'control2'])
sg.add_line('Unit FE', ['No', 'Yes', 'Yes'])
sg.add_line('Year FE', ['No', 'Yes', 'Yes'])
sg.significant_digits(3)
print(sg.render_latex())
```

### Event Study Plot

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Assumes: coefs (array), ses (array), periods (array, e.g. -5 to 5)
fig, ax = plt.subplots(figsize=(8, 4))
ax.errorbar(periods, coefs, yerr=1.96*ses,
            fmt='o-', color='steelblue', capsize=4, linewidth=1.5)
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(-0.5, color='red', linewidth=0.8, linestyle=':', label='Treatment')
ax.set_xlabel('Years Relative to Treatment')
ax.set_ylabel('Estimated Effect (95% CI)')
ax.set_title('Event Study: Dynamic Treatment Effects')
ax.legend()
plt.tight_layout()
plt.savefig('figures/event_study.pdf', bbox_inches='tight')
```

---

## Package Installation

```bash
# Install all causal inference tools at once
uv pip install linearmodels pyfixest econml doubleml rdrobust rddensity stargazer

# For synthetic control
uv pip install pysynth  # or: pip install synth_runner

# Stata bridge (if needed)
uv pip install pystata pyreadstat
```

---

## Reference Resources

- **`references/stata-to-python.md`** — Comprehensive Stata→Python translation with code
- **`references/identification-tests.md`** — Detailed assumption test protocols (pre-trends, density, first stage)
- **`references/output-templates.md`** — LaTeX table templates, event study plot templates
