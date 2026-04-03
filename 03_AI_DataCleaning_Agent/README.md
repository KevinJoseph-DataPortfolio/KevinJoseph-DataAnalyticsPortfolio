# 🤖 AI-Powered Lab Data Cleaning Agent

> Query 10,000 rows of dirty lab data in plain English — no cleaning required.

---

## What This Project Does

Real-world lab data is messy. Mixed casing, inconsistent date formats, missing values, duplicate IDs — all at the same time. Most analysts clean the data first, then analyze it. This agent skips that step entirely.

You ask a question in natural language. The agent answers with exact numbers and insights — despite the mess.

---

## Live Demo

Ask things like:

| Question | Answer |
|----------|--------|
| How many non-compliant samples? | **1,925** non-compliant out of 7,526 known statuses (25.6%) |
| Which site has the worst compliance? | **Marseille** — 21.1% non-compliance rate |
| Top non-compliant product? | **Amoxicillin** — 73 non-compliant cases |
| Average pH by category? | Ranges from **5.94** (Processed Food) to **6.06** (Beverages) |
| How many missing values? | **11,349** across all columns |

---

## Architecture

```
lab_quality_data_RAW_EN.csv  (10,000 dirty rows)
            ↓
    lab_ai_agent.py
    (Anthropic Claude API)
            ↓
  Natural language answers
  — no cleaning, no code shown
```

---

## Dataset Overview

| Metric | Value |
|--------|-------|
| Total rows | 10,000 |
| Columns | 13 |
| Duplicate Sample IDs | 494 |
| Missing values | 11,349 |
| Date formats | 5 different formats |
| Unit inconsistencies | 1,565 rows |
| Data quality score | 91.3% |

**Intentional data issues:**
- Mixed casing (`Compliant` / `compliant` / `COMPLIANT`)
- Multiple date formats (`DD/MM/YYYY`, `YYYY-MM-DD`, `MM-DD-YYYY`...)
- Inconsistent units (`mg/L`, `MG/L`, `ug/L`, `µg/L`)
- Numeric outliers (negative values, values > 9999)
- Inconsistent temperature formats (`5°C`, `5 C`, `5°`, `5`)

---

## Key Findings (from dirty data)

- **Overall compliance rate: 24.1%** — only 1 in 4 samples is compliant
- **Worst site: Marseille** (21.1% non-compliance), **best: Bordeaux** (17.5%)
- **Most non-compliant product: Amoxicillin** — flags a pharma quality issue
- **Bordeaux** has the highest average bacteriological contamination (514.9)
- **30% of Operator records are missing** — traceability risk

---

## Files

```
03_AI_DataCleaning_Agent/
├── lab_quality_data_RAW_EN.csv   — Dirty dataset (10,000 rows)
├── lab_ai_agent.py               — AI agent (Python + Claude API)
├── requirements.txt              — Dependencies
└── README.md                     — This file
```

---

## How to Run

```bash
# Install dependencies
pip install anthropic pandas

# Set your API key
export ANTHROPIC_API_KEY=your_key_here

# Run the agent
python lab_ai_agent.py
```

---

## Tools & Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude_API-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green)

---

## Why This Matters for Business

In regulated industries (food, pharma, biotech), quality managers need answers fast. They can't wait for a data analyst to clean a dataset before querying it. This agent removes that bottleneck — giving any stakeholder direct access to insights from raw, unprocessed data.

---

*Built by [Kévin Joseph](https://linkedin.com/in/kevin-joseph) | Data Analyst Portfolio*
