# Custora – RFM Customer Segmentation & Retention Analysis

End-to-end customer analytics project using the UCI Online Retail dataset (2010–2011).  
The goal was to clean transactional data, explore patterns, segment customers using the RFM framework, and provide actionable retention & marketing recommendations.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-1.5%2B-green?style=flat&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Seaborn-Data%20Viz-orange?style=flat&logo=seaborn" alt="Seaborn">
  <img src="https://img.shields.io/badge/Google%20Colab-Ready-F9AB00?style=flat&logo=googlecolab" alt="Colab">
</p>

## Project Structure
Custora/
├── notebooks/
│   ├── Custora_data_cleaning.ipynb     # Phase 1: Data cleaning & preprocessing
│   ├── Custora_EDA.ipynb               # Phase 2: Exploratory Data Analysis
│   └── Custora_RFM.ipynb               # Phase 3: RFM calculation, scoring, segmentation & recommendations
├── data/
│   ├── online_retail.csv               # Original raw dataset (~34 MB – download from UCI if needed)
│   ├── clean_online_retail.csv         # Cleaned & filtered transactions
│   └── rfm_segments.csv                # Final customer-level RFM table with segments
└── README.md
> **Note on large file**: `data/online_retail.csv` (>25 MB) is not previewable in GitHub.  
> Download from Kaggle:  
> https://www.kaggle.com/datasets/carrie1/ecommerce-data  
> or UCI: https://archive.ics.uci.edu/dataset/352/online+retail

## Business Problem & Objective

Online retail businesses struggle with customer churn and inefficient marketing spend.  
This project answers:

- Who are our most valuable customers?
- Which customers are at risk of leaving?
- How can we prioritize retention and reactivation efforts?

## Methodology

1. **Data Cleaning**  
   Removed cancellations, negative quantities/prices, missing CustomerIDs, duplicates.

2. **Exploratory Data Analysis**  
   - Revenue by country & month  
   - Customer concentration (Pareto)  
   - Transaction value distribution

3. **RFM Analysis**  
   - **Recency** — days since last purchase  
   - **Frequency** — number of transactions  
   - **Monetary** — total spend  
   → Manual binning for scores (R/F/M 1–5) due to skewed frequency distribution  
   → Rule-based segmentation (Champions, Loyal, At Risk, Lost, etc.)

4. **Business Recommendations**  
   Targeted actions for each segment (VIP programs, win-back campaigns, welcome series, etc.)

## Key Results

- **Champions** (~21%) → very high frequency & spend (~$6,678 avg)  
- **Recent Customers** (~27%) → largest group, but mostly one-time buyers  
- ~26% of customers are **Lost / At Risk / Hibernating** → high churn potential  
- Top ~40% of customers (Champions + Loyal) drive the majority of revenue

## How to Run the Project

1. Clone the repository
   ```bash
   git clone https://github.com/TanjinaAhmed/Custora.git
2. Open any notebook in Google Colab or locally (Jupyter / VS Code)
Start with Custora_data_cleaning.ipynb if you want to reproduce from raw data
Or go directly to Custora_RFM.ipynb for segmentation & recommendations
3. All notebooks are self-contained and use only standard libraries (pandas, matplotlib, seaborn).

## Technologies Used

- Python 3.8+
- pandas, numpy
- matplotlib, seaborn
- Google Colab (development environment)

## Learnings & Takeaways

- Handling real-world messy retail data (cancellations, missing values, outliers)
- Why automatic quintiles fail on skewed Frequency → importance of custom binning
- Translating RFM scores into business actions (retention marketing perspective)
- Organizing data science projects for reproducibility & sharing

## Future Improvements (planned / ideas)

- Cohort-based retention rate analysis
- K-means or hierarchical clustering on RFM scores
- Simple Streamlit / Dash dashboard for segment exploration
- Predictive churn modeling (logistic regression / XGBoost)

Author
Tanjina Ahmed Mitu
Data Science Enthusiast | Dhaka, Bangladesh
GitHub | LinkedIn
Feel free to fork, star ⭐ or open an issue if you have questions or suggestions.
Last updated: February 2025


