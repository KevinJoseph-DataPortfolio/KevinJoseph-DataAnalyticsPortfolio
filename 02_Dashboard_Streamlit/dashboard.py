import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cancer Risk Factors", layout="wide")

st.title("🔬 Cancer Risk Factors — Interactive Dashboard")
st.markdown("**Dataset:** Kaggle · **Tools:** Python · Streamlit · Plotly")

df = pd.read_csv("02_Dashboard_Streamlit/cancer-risk-factors.csv")

# --- FILTRES ---
st.sidebar.header("Filters")
cancer_types = st.sidebar.multiselect("Cancer Type", df["Cancer_Type"].unique(), default=df["Cancer_Type"].unique())
risk_levels = st.sidebar.multiselect("Risk Level", df["Risk_Level"].unique(), default=df["Risk_Level"].unique())
df = df[df["Cancer_Type"].isin(cancer_types) & df["Risk_Level"].isin(risk_levels)]

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Patients", len(df))
col2.metric("Avg Age", f"{df['Age'].mean():.0f} yrs")
col3.metric("Avg Risk Score", f"{df['Overall_Risk_Score'].mean():.2f}")
col4.metric("Avg BMI", f"{df['BMI'].mean():.1f}")

st.divider()

# --- GRAPHIQUES ---
col_a, col_b = st.columns(2)

with col_a:
    fig1 = px.histogram(df, x="Age", color="Risk_Level",
                        title="Age Distribution by Risk Level",
                        color_discrete_map={"Low":"green","Medium":"orange","High":"red"})
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    fig2 = px.scatter(df, x="Air_Pollution", y="Overall_Risk_Score",
                      color="Risk_Level", title="Air Pollution vs Risk Score",
                      color_discrete_map={"Low":"green","Medium":"orange","High":"red"})
    st.plotly_chart(fig2, use_container_width=True)

col_c, col_d = st.columns(2)

with col_c:
    fig3 = px.box(df, x="Cancer_Type", y="Overall_Risk_Score",
                  title="Risk Score by Cancer Type", color="Cancer_Type")
    st.plotly_chart(fig3, use_container_width=True)

with col_d:
    fig4 = px.histogram(df, x="Risk_Level", color="Risk_Level",
                        title="Risk Level Distribution",
                        color_discrete_map={"Low":"green","Medium":"orange","High":"red"})
    st.plotly_chart(fig4, use_container_width=True)

st.caption("Built by Kévin Joseph | Data Analyst Portfolio")
