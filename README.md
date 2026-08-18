# Supply Chain Performance Analysis

## Overview

This project analyzes the DataCo Global Supply Chain dataset to investigate
the relationship between delivery performance and order profitability. The
central questions are whether late deliveries meaningfully affect profit margins
and which operational factors — shipping mode, delivery status, and order timing
— drive the most significant differences in supply chain profitability.

The findings reveal that while shipping mode is strongly associated with late
delivery risk, late delivery itself does not significantly reduce profitability
— a counterintuitive result with real operational implications.

---

## Central Questions

- Does shipping mode significantly affect delivery performance?
- Does late delivery significantly affect order profitability?
- Is profitability meaningfully different across shipping modes?
- Does profitability vary significantly by month?

---

## Key Findings

| Question | Test Used | Result |
|---|---|---|
| Shipping mode vs late delivery | Chi-squared | χ² = 37,716 — p = 0.0000 — **significant association** |
| Late delivery vs profit | Independent t-test + Mann-Whitney U | p = 0.1156 / p = 0.2106 — **no significant difference** |
| Profit across shipping modes | One-way ANOVA | F = 1.98 — p = 0.1147 — **no significant difference** |
| Profit variation by month | One-way ANOVA | F = 2.54 — p = 0.0033 — **significant variation** |

### Notable EDA Observations

- **Standard Class** is the dominant shipping mode — used in the majority of
  all orders, overshadowing the other three modes combined
- **First Class** generates the highest average profit per order
- **Same Day** generates the lowest average profit per order
- **Standard Class** generated the most total loss in absolute terms
- **October** consistently generated the highest average profit across
  2015–2018
- **Shipping cancelled** orders generate the most loss on average per order
- **18,942 outliers** detected in benefit_per_order using IQR method

### The Counterintuitive Finding

Despite shipping mode being strongly associated with late delivery risk
(p = 0.0000), late delivery itself does not significantly reduce profitability
(p = 0.1156 and p = 0.2106 across two independent tests). This suggests that
the financial cost of late delivery may be absorbed elsewhere in the supply
chain rather than directly reducing per-order profit margins.

---

## Dataset

- **Source:** DataCo Global Supply Chain Dataset (publicly available)
- **Scale:** 180,519 orders across multiple global markets
- **Period:** 2015–2018
- **Markets:** Pacific Asia, South Asia, Europe, Americas, Africa
- **Duplicates:** None found
- **Key nulls:** Order Zipcode (86% missing — excluded from analysis),
  Product Description (100% missing — dropped)

---

## Tools Used

| Tool | Purpose |
|---|---|
| SQL Server | Data storage and querying |
| Python | Data ingestion, cleaning, and statistical analysis |
| Pandas | Data manipulation |
| Seaborn / Matplotlib | Visualization |
| SciPy | Statistical testing |
| Git / GitHub | Version control |

---

## Statistical Methods

- **Chi-squared test of independence** — association between categorical variables
- **Independent samples t-test (Welch's)** — difference in means between two groups
- **Mann-Whitney U test** — non-parametric alternative for skewed distributions
- **One-way ANOVA** — difference in means across three or more groups
- **IQR method** — outlier detection

---

## Repository Structure

```
Supply-Chain-Performance-Analysis/
├── dashboards/
├── data/
│   └── raw/
│       └── DataCoSupplyChainDataset.csv
├── notebooks/
│   ├── 01_ingestion_and_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_analyses.ipynb
├── scripts/
│   ├── __init__.py
│   └── cleaning.py
├── .gitignore
└── README.md
```

---

## Limitations

- Dataset covers 2015–2018
- Synthetic elements suspected in some fields
- Order Zipcode is 86% null — geographic granularity at zip code level is not
  possible
- No cost-of-shipping data — cannot compute true net margin per order
- Causation cannot be established from observational data alone

---

## Setup

**Prerequisites:**
- Python 3.x with pandas, numpy, matplotlib, seaborn, scipy, sqlalchemy, pyodbc
- SQL Server with SSMS
- ODBC Driver 18 for SQL Server

**Steps:**
1. Clone the repository
2. Place `DataCoSupplyChainDataset.csv` in `data/raw/`
3. Create a database named `SupplyChainDB` in SQL Server via SSMS
4. Run `notebooks/01_ingestion_and_cleaning.ipynb` to load and clean data
5. Run `notebooks/02_eda.ipynb` for exploratory analysis
6. Run `notebooks/03_analyses.ipynb` for statistical testing

---

## Author

**Jan Brix Ilan**
Mathematics educator transitioning into Data Analytics | Supply Chain Focus

[LinkedIn](https://www.linkedin.com/in/jan-brix-ilan-6973b725b/) |
[GitHub](https://github.com/JanBrixIlan)
