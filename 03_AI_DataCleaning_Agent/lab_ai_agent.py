"""
Lab Quality AI Agent
====================
AI-powered chat interface to query dirty lab quality control data
in natural language — no data cleaning required.

Stack    : Python · Anthropic Claude API · Pandas
Industry : Food & Biotech Quality Control
Author   : Kévin Joseph | Data Analyst Portfolio
"""

import anthropic
import pandas as pd

CSV_URL = "https://raw.githubusercontent.com/KevinJoseph-DataPortfolio/KevinJoseph-DataAnalyticsPortfolio/main/03_AI_DataCleaning_Agent/lab_quality_data_RAW_EN.csv"

def load_data(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    print(f"✅ Dataset loaded: {len(df):,} rows, {len(df.columns)} columns")
    print(f"   Missing values : {df.isnull().sum().sum():,}")
    print(f"   Duplicate IDs  : {df['Sample_ID'].duplicated().sum()}")
    return df

def build_system_prompt(df: pd.DataFrame) -> str:
    sample = df.sample(min(80, len(df)), random_state=42)
    sample_csv = sample.to_csv(index=False)

    return f"""You are a senior data analyst working with a real-world dirty lab quality control dataset
from a food & biotech company. The data has NOT been cleaned — it contains mixed casing,
multiple date formats, inconsistent units, missing values, and duplicate IDs. This is intentional.

DATASET OVERVIEW:
- Total rows     : {len(df):,}
- Columns        : {', '.join(df.columns)}
- Missing values : {df.isnull().sum().sum():,}
- Duplicate IDs  : {df['Sample_ID'].duplicated().sum()}

DATA SAMPLE (representative subset of {len(sample)} rows):
{sample_csv}

RULES:
1. NEVER show Python code. Give only the final answer in plain English.
2. Ignore case when filtering: "Compliant" = "compliant" = "COMPLIANT"
3. Treat location variants as the same: "Paris" = "paris" = "PARIS"
4. Exclude null/missing values from counts unless specifically asked about them.
5. Use the sample to estimate answers. Clearly state if your answer is an estimate.
6. Format numbers with commas. Use **bold** for key findings.
7. Keep answers under 150 words. Be direct and professional."""

def chat(df: pd.DataFrame):
    client = anthropic.Anthropic()
    system_prompt = build_system_prompt(df)
    history = []

    print("\n" + "="*55)
    print("   LAB QUALITY AI AGENT — Ready")
    print("   Type 'exit' to quit")
    print("="*55 + "\n")

    while True:
        question = input("You: ").strip()
        if question.lower() in ("exit", "quit", "q"):
            print("Session ended.")
            break
        if not question:
            continue

        history.append({"role": "user", "content": question})

        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            system=system_prompt,
            messages=history
        )

        answer = response.content[0].text
        history.append({"role": "assistant", "content": answer})

        print(f"\nAgent: {answer}\n")

if __name__ == "__main__":
    df = load_data(CSV_URL)
    chat(df)
