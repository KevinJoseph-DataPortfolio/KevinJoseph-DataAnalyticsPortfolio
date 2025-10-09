# Data Cleaning & EDA – Cancer Risk Factors  
*(Dataset in English, source: Kaggle)*  

---

## Goal  
Transform a raw health dataset into clean, interpretable insights.  
This project identifies which lifestyle, demographic, and environmental factors are most correlated with cancer risk.

---

## ⚙️ Project Overview  

### 1️⃣ Data Sources  
- **Raw dataset:** [`cancer-risk-factors.csv`](./data/cancer-risk-factors.csv)  
- **Cleaned dataset:** [`cancer-risk-factors-cleaned.xlsx`](./data/cancer-risk-factors-cleaned.xlsx) *(cleaned with Power Query)*  

### 2️⃣ Data Cleaning  
- Standardized column names  
- Removed missing values and duplicates  
- Fixed inconsistent datatypes  
- Basic feature formatting (percentages, numeric values)  

### 3️⃣ Exploratory Data Analysis (EDA)  
Performed with **Python** (see [`EDA_Cancer_Risk.ipynb`](./notebooks/EDA_Cancer_Risk.ipynb)):  
- Descriptive statistics  
- Correlation heatmap  
- Visualization of main risk factors (smoking, alcohol, pollution, age, etc.)  
- Identification of top correlated features  

### 4️⃣ Business Insights  
See summary slide: [`Cancer_Risk_Factors_Analysis.pptx`](./visuals/Cancer_Risk_Factors_Analysis.pdf)  
- Environmental exposure and smoking rate drive highest risk
