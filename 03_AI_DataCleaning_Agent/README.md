# 🤖 AI-Powered Lab Data Cleaning Agent

## Overview
Automated data cleaning pipeline for lab quality control data 
in food & biotech industries.

## Architecture
Flowise AI (analysis) → Python/Pandas (cleaning) → Streamlit (dashboard)

## Results
| Metric | Before | After |
|--------|--------|-------|
| Rows | 10,000 | 9,506 |
| Duplicates | 494 | 0 |
| Missing values | 11,349 | 0 |
| Data quality score | 91.3% | 100% |

## Tools
Python · Pandas · Flowise AI · Groq LLM · Streamlit

## Files
- `lab_quality_data_RAW_EN.csv` — Raw dirty dataset (10,000 rows)
- `lab_quality_data_CLEAN.csv` — Cleaned dataset (9,506 rows)
- `cleaning_pipeline.ipynb` — Full cleaning notebook

Built by Kévin Joseph | Data Analyst Portfolio
