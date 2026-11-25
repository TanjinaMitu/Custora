# 🛍️ Custora — RFM Customer Segmentation & Retention Analytics

End-to-end customer analytics and interactive retention dashboard built on the **UCI Online Retail Dataset (2010–2011)**. This project transforms **540K+ raw transactional records** into a clean **4,338-customer ($8.91M revenue)** RFM segmentation model, business SQL queries, and a live Streamlit decision-support web application.

🔗 **Live Interactive Dashboard:** `<https://tanjina-custora-rfm.streamlit.app/>`

---

## 🎯 Business Problem & Objectives
Online retail businesses frequently lose revenue to silent customer churn and unfocused promotional spending. **Custora** answers three core commercial questions:
* **Who are our most valuable customers?** Identifying high-spend, high-frequency buyers driving core revenue.
* **Which customers are at risk of churning?** Detecting previously active or high-spending buyers whose recency is slipping.
* **How should marketing allocate retention budgets?** Mapping every customer segment to concrete, cost-effective lifecycle campaigns.

---

## 📊 Key Analytical Findings
* **Extreme Pareto Revenue Concentration:** **Champions** (901 customers, 20.8%) and **Loyal Customers** (824 customers, 19.0%) account for **39.8% of the customer base** but generate **79.6% of total revenue** (**67.5%** and **12.1%**, respectively).
* **High-Volume Onboarding Opportunity:** **Recent Customers** represent the largest single segment (**1,164 buyers**, 26.8%), highlighting a major opportunity to convert first-time buyers into repeat purchasers via automated onboarding sequences.
* **Actionable Churn & Win-Back Pool:** **1,115 customers (25.7%)** fall into **Lost** (620), **Hibernating** (347), or **At Risk** (148) tiers. Specifically, the **148 At-Risk buyers** average **$625.25 in spend** with **250 days since their last order**, making them high-ROI targets for immediate win-back campaigns.

---

## 🗂️ Project Structure
```text
Custora/
├── app.py                          # Interactive Streamlit & Plotly retention dashboard
├── requirements.txt                # Production Python dependencies
├── .gitignore                      # Excludes virtual environments and large raw CSVs
├── sql/
│   └── rfm_business_queries.sql    # Executive KPI & priority win-back SQL queries
├── notebooks/
│   ├── Custora_data_cleaning.ipynb # Phase 1: Data cleaning & anomaly filtering
│   ├── Custora_EDA.ipynb           # Phase 2: Exploratory Data Analysis & Pareto trends
│   └── Custora_RFM.ipynb           # Phase 3: RFM scoring, binning & rule-based segmentation
├── data/
│   └── rfm_segments.csv            # Final customer-level RFM scores & segments (4,338 rows)
└── README.md
```

> **Note on Raw Data:** Raw transactional files (`online_retail.csv` and `clean_online_retail.csv`) exceed GitHub's preview limits and are excluded via `.gitignore`. To reproduce Phase 1–2 from scratch, download the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail) or [Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data) and place `online_retail.csv` inside `data/`.

---

## ⚙️ Methodology
1. **Data Cleaning (`Custora_data_cleaning.ipynb`):** Removed cancelled invoices (`InvoiceNo` starting with `'C'`), negative/zero quantities and unit prices, duplicate records, and rows missing `CustomerID`.
2. **Exploratory Data Analysis (`Custora_EDA.ipynb`):** Analyzed geographic revenue distribution, monthly seasonality, order value distributions, and customer revenue concentration.
3. **RFM Feature Engineering & Segmentation (`Custora_RFM.ipynb`):**
   * Calculated **Recency** (days since last purchase), **Frequency** (distinct order count), and **Monetary** (total revenue) per customer.
   * Applied **domain-informed custom binning** (1–5 scale) rather than blind quantiles to handle right-skewed purchase frequency distributions.
   * Classified customers into **9 actionable segments**: *Champions, Loyal Customers, Big Spenders, Frequent Buyers, Recent Customers, Need Attention, At Risk, Hibernating,* and *Lost*.
4. **SQL & Interactive BI Layer (`sql/` & `app.py`):** Built analytical SQL queries for segment KPI aggregation and churn target extraction, paired with a Streamlit dashboard for dynamic filtering, retention playbook lookup, and CSV list export.

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TanjinaMitu/Custora.git
   cd Custora
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies and launch the dashboard:**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

---

## 🛠️ Tech Stack
* **Languages & Querying:** Python 3.13, SQL
* **Data Processing & Analysis:** Pandas, NumPy
* **Visualization & App Deployment:** Streamlit, Plotly, Matplotlib, Seaborn
* **Development Environment:** VS Code, Jupyter Notebooks, Google Colab, Git/GitHub

---

## 🔮 Future Enhancements
* **Cohort Retention Analysis:** Track month-over-month customer retention curves across acquisition cohorts.
* **Unsupervised Clustering:** Benchmark rule-based RFM tiers against K-Means and hierarchical clustering.
* **Predictive Churn Modeling:** Train a classification model (Logistic Regression / XGBoost) to estimate 90-day churn probability.