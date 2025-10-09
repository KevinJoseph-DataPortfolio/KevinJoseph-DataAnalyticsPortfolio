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
- Save a clean version: `cancer-risk-factors-cleaned.xlsx`.

### 2️⃣ Data Cleaning (Python / Pandas)  
- Handle missing values and outliers.  
- Standardize column names.  
- Remove duplicates and verify consistency.  

### 3️⃣ Exploratory Data Analysis (EDA)  
- Visualize variable distributions (smoking, alcohol, pollution, etc.)  
- Compute correlations between factors and cancer risk.  
- Highlight patterns and regional trends.

### 4️⃣ Visualization & Reporting  
- Create charts and a heatmap using **Matplotlib** and **Seaborn**.  
- Design a one-page **PDF summary** with key findings and visuals.

---

## Tools Used  
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-yellow)
![PowerQuery](https://img.shields.io/badge/Excel-Power%20Query-00751A)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red)

---

## Project Files  

| Type | File | Description |
|------|------|-------------|
| 📄 Raw Data | [cancer-risk-factors.csv](./data/cancer-risk-factors.csv) | Original Kaggle dataset |
| 📊 Cleaned Data | [cancer-risk-factors-cleaned.xlsx](./data/cancer-risk-factors-cleaned.xlsx) | Processed with Power Query |
| 📓 Notebook | [EDA_Cancer_Risk.ipynb](./notebooks/EDA_Cancer_Risk.ipynb) | Python-based data analysis |
| 📈 Visuals | [View charts folder](./visuals) | PNG charts and heatmaps |
| 🧾 Slides | [Cancer Risk Analysis Summary (PDF)](./slides/Cancer_Risk_Analysis_Summary.pdf) | One-slide summary of insights |

---

## Key Insights
- Pollution, smoking, and alcohol use show positive correlation with cancer incidence.  
- Regions with higher healthcare access tend to show earlier detection and lower mortality.  
- Preventive awareness programs appear underrepresented in high-risk zones.

---

> *This project shows end-to-end analytical thinking: from raw data to actionable insight, blending technical rigor and business clarity.*
