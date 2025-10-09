# Data Cleaning & Exploratory Data Analysis – Cancer Risk Factors  
*(Dataset in English, source: Kaggle)*  

---

## Project Goal  
Analyze how lifestyle, environmental, and demographic factors relate to cancer risk across regions.  
The objective is to demonstrate a complete data workflow — from raw dataset to insights — using **Python**, **Excel (Power Query)**, and **visual storytelling**.

---

## Project Workflow  

### 1️⃣ Data Collection & Preparation  
- Import the original CSV file from Kaggle.  
- Load and clean the dataset using **Power Query (Excel)**.  
- Save a clean version: `cancer_risk_factor.xlsx`.

📄 [Raw dataset (CSV)](./data/cancer-risk-factors.csv)  
📊 [Cleaned dataset (Excel)](./data/cancer_risk_factor.xlsx)

---

### 2️⃣ Data Cleaning (Python / Pandas)  
- Handle missing values and outliers.  
- Standardize column names.  
- Remove duplicates and verify consistency.  

📓 [Jupyter Notebook – EDA_Cancer_Risk.ipynb](./notebooks/EDA_Cancer_Risk.ipynb)

---

### 3️⃣ Exploratory Data Analysis (EDA)  
- Distribution of key variables (age, alcohol, air pollution, smoking, etc.)  
- Correlation heatmap between risk factors and cancer prevalence.  
- Insights extracted from visual trends.

📈 [Visuals folder](./visuals)  
Exemples :
- [Age distribution](./visuals/Age_dist.png)  
- [Air pollution distribution](./visuals/Air_Pollution_dist.png)  
- [Alcohol consumption distribution](./visuals/Alcohol_dist.png)  

---

### 4️⃣ Visualization & Reporting  
- Summary slide presenting key findings and visuals.  
📑 [Key Findings – Cancer Risk Factors (PDF)](./slides/Key%20Findings%20-%20Cancer%20Risk%20Factors.pdf)

---

## Tools Used  
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-yellow)
![Excel](https://img.shields.io/badge/Excel-Power%20Query-00751A)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red)

---

## Key Insights (summary)
- Pollution, smoking, and alcohol consumption correlate positively with cancer risk.  
- Countries with better healthcare infrastructure show lower mortality rates.  
- Preventive awareness programs significantly impact long-term outcomes.

---

> *This project demonstrates the full workflow of a data analyst: collecting, cleaning, exploring, and presenting data-driven insights clearly and effectively.*
