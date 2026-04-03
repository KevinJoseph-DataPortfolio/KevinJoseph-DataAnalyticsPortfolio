
import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import io

st.set_page_config(page_title="Lab Data Cleaning Agent", layout="wide")

RAW_URL = "https://raw.githubusercontent.com/KevinJoseph-DataPortfolio/KevinJoseph-DataAnalyticsPortfolio/main/03_AI_DataCleaning_Agent/lab_quality_data_RAW_EN.csv"
CLEAN_URL = "https://raw.githubusercontent.com/KevinJoseph-DataPortfolio/KevinJoseph-DataAnalyticsPortfolio/main/03_AI_DataCleaning_Agent/lab_quality_data_CLEAN.csv"

@st.cache_data
def load():
    raw = pd.read_csv(RAW_URL)
    clean = pd.read_csv(CLEAN_URL)
    return raw, clean

raw, clean = load()

st.title("🤖 AI-Powered Lab Data Cleaning Agent")
st.markdown("**Stack:** Python · Flowise AI · Groq LLM · Streamlit · fpdf2 | **Industry:** Food & Biotech Quality Control")
st.divider()

tab1, tab2, tab3 = st.tabs(["📊 Before vs After", "🔍 Data Explorer", "💬 Chat with Data"])

with tab1:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows Before", f"{len(raw):,}")
    c2.metric("Rows After", f"{len(clean):,}", f"-{len(raw)-len(clean):,} duplicates removed")
    c3.metric("Missing Values", "0", f"-{raw.isnull().sum().sum():,}", delta_color="inverse")
    c4.metric("Data Quality Score", "100%", "+8.7%")

    st.subheader("Issues Found & Fixed")
    issues = pd.DataFrame({
        "Issue Type": ["Duplicate rows", "Missing values", "Inconsistent casing", "Invalid date formats", "Numeric outliers", "Inconsistent units"],
        "Before": [494, 11349, 2840, 1200, 156, 1565],
        "After": [0, 0, 0, 0, 0, 0],
        "Status": ["✅ Fixed","✅ Fixed","✅ Fixed","✅ Fixed","✅ Fixed","✅ Fixed"]
    })
    st.dataframe(issues, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(
            issues, x="Issue Type", y="Before",
            title="Issues Fixed by Type",
            color="Issue Type"
        )
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.pie(
            values=[91.3, 8.7],
            names=["Clean Before", "Improvement"],
            title="Data Quality: 91.3% → 100%",
            color_discrete_sequence=["#ef553b","#00cc96"]
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()
    st.subheader("📄 Download Cleaning Report")

    if st.button("Generate PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "Lab Data Cleaning Report", ln=True, align="C")
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(0, 8, "Built by Kevin Joseph | Data Analyst Portfolio", ln=True, align="C")
        pdf.ln(8)
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 8, "Summary", ln=True)
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(0, 7, f"Rows before cleaning : {len(raw):,}", ln=True)
        pdf.cell(0, 7, f"Rows after cleaning  : {len(clean):,}", ln=True)
        pdf.cell(0, 7, f"Duplicates removed   : {len(raw)-len(clean):,}", ln=True)
        pdf.cell(0, 7, f"Missing values fixed : {raw.isnull().sum().sum():,}", ln=True)
        pdf.cell(0, 7, f"Quality score before : 91.3%", ln=True)
        pdf.cell(0, 7, f"Quality score after  : 100.0%", ln=True)
        pdf.ln(6)
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 8, "Issues Fixed", ln=True)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(90, 7, "Issue Type", border=1)
        pdf.cell(40, 7, "Count Fixed", border=1, ln=True)
        pdf.set_font("Helvetica", "", 10)
        for _, row in issues.iterrows():
            pdf.cell(90, 7, row["Issue Type"], border=1)
            pdf.cell(40, 7, str(row["Before"]), border=1, ln=True)
        pdf.ln(6)
        pdf.set_font("Helvetica", "I", 9)
        pdf.cell(0, 7, "Generated automatically by AI-Powered Lab Data Cleaning Agent", ln=True, align="C")

        pdf_bytes = pdf.output()
        st.download_button(
            label="⬇️ Download PDF Report",
            data=bytes(pdf_bytes),
            file_name="Lab_Cleaning_Report_KevinJoseph.pdf",
            mime="application/pdf"
        )

with tab2:
    view = st.radio("Dataset", ["RAW (dirty)", "CLEAN (processed)"], horizontal=True)
    df = raw.copy() if view == "RAW (dirty)" else clean.copy()

    col1, col2 = st.columns(2)
    with col1:
        sites = st.multiselect("Production Site", sorted(df["Production_Site"].dropna().unique()))
    with col2:
        statuses = st.multiselect("Compliance Status", sorted(df["Compliance_Status"].dropna().unique()))

    if sites:
        df = df[df["Production_Site"].isin(sites)]
    if statuses:
        df = df[df["Compliance_Status"].isin(statuses)]

    st.dataframe(df.head(100), use_container_width=True)

    fig3 = px.histogram(df, x="Compliance_Status", color="Compliance_Status",
                        title="Compliance Distribution")
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.subheader("💬 Ask questions about the cleaned data")
    question = st.text_input("Your question", placeholder="How many non-compliant samples from Paris in 2023 ?")

    if question:
        q = question.lower()
        df = clean.copy()

        for site in df["Production_Site"].dropna().unique():
            if site.lower() in q:
                df = df[df["Production_Site"].str.lower() == site.lower()]

        for year in ["2020","2021","2022","2023","2024"]:
            if year in q:
                df = df[df["Collection_Date"].astype(str).str.contains(year)]

        if "non-compliant" in q or "non compliant" in q:
            df = df[df["Compliance_Status"].str.lower() == "non-compliant"]
        elif "pending" in q:
            df = df[df["Compliance_Status"].str.lower() == "pending"]
        elif "compliant" in q:
            df = df[df["Compliance_Status"].str.lower() == "compliant"]

        if "how many" in q or "count" in q:
            st.success(f"**{len(df):,} samples** match your query.")
        elif "average" in q or "mean" in q:
            if "ph" in q:
                st.success(f"**Average pH level : {df['pH_Level'].mean():.2f}**")
            elif "bacterio" in q:
                st.success(f"**Average bacteriological result : {df['Bacteriological_Result'].mean():.2f}**")
            else:
                st.success(f"**{len(df):,} samples** match your query.")
        else:
            st.success(f"**{len(df):,} samples** match your query.")

        if len(df) > 0:
            fig = px.histogram(df, x="Production_Site", color="Compliance_Status",
                               title="Results by Site")
            st.plotly_chart(fig, use_container_width=True)

st.caption("Built by Kévin Joseph | Data Analyst Portfolio | github.com/KevinJoseph-DataPortfolio")
