<h1 align="center">📊 Vendor Performance Data Analysis</h1>

---

<h3 align="center">🔖 Repo Stats</h3>
<p align="center">
  <img src="https://img.shields.io/github/last-commit/SheikhNoor/Vendor-Performance-Data-Visualisation" alt="Last Commit">
  <img src="https://img.shields.io/github/languages/top/SheikhNoor/Vendor-Performance-Data-Visualisation" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/SheikhNoor/Vendor-Performance-Data-Visualisation" alt="Language Count">
 
</p>
<h3 align="center">🧑‍💻 Languages Used</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8-blue" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange" alt="Jupyter Notebook">
  <img src="https://img.shields.io/badge/SQL-SQLAlchemy-lightgrey" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/PowerBI-Dashboard-yellow" alt="Power BI">
</p>

---

## 📑 Table of Contents

- [✅ Project Overview](#✅-project-overview)
- [📂 Dataset & Scale](#📂-dataset--scale)
- [✅ How the Data is Used](#✅-how-the-data-is-used)
- [🚀 Features](#🚀-features)
- [📂 Project Structure](#📂-project-structure)
- [⚙️ Setup Instructions](#⚙️-setup-instructions)
- [📊 Key Metrics](#📊-key-metrics)
- [📈 Insights](#📈-insights)
- [📂 Logging](#📂-logging)
- [📱 Connect with Me](#📱-connect-with-me)
- [📜 License](#📜-license)
- [🚀 Future Enhancements](#🚀-future-enhancements)

---

## ✅ Project Overview

This project analyzes and visualizes vendor performance using a large dataset comprising approximately **15 million records**. These records span purchases, sales, freight charges, and pricing details across multiple vendors and brands. The goal is to extract actionable insights that help:

- Optimize vendor relationships  
- Improve purchasing strategies  
- Enhance profitability  
- Manage inventory efficiently  
- Detect anomalies and inefficiencies  

The project is designed with scalability in mind, using chunk-based data processing and efficient algorithms to ensure smooth operation even with massive datasets.

---

## 📂 Dataset & Scale

The project uses **six datasets** with the following details:

| Table                | Description                                      | Approximate Rows | Size       |
|----------------------|-------------------------------------------------|----------------|-----------|
| `purchases.csv`       | Purchase orders with quantity, price, vendor info | 2,372,474      | 344 MB    |
| `sales.csv`           | Transaction data including revenue and taxes     | 12,825,363     | 1.48 GB   |
| `vendor_invoice.csv`  | Freight and logistical costs per shipment        | 5,543          | 498 KB    |
| `purchase_prices.csv` | Pricing details including volume-based discounts | 12,261         | 0.99 MB   |
| `begin_inventory.csv` | Beginning inventory records                       | 206,529        | 16.6 MB   |
| `end_inventory.csv`   | Ending inventory records                           | 224,489        | 18.1 MB   |

**Total approximate rows:** ~15.7 million  
**Total volume:** ~1.86 GB  

> ⚡ **Note:** Large datasets like `purchases.csv` and `sales.csv` are processed in **chunks of 100,000 rows** for efficient memory management.  
---

## ✅ How the Data is Used

### Real-World Scenarios

- **Identifying underperforming vendors**  
  Analyze metrics like gross profit and stock turnover to spot vendors with stagnant or unprofitable inventory.

- **Optimizing bulk purchases**  
  Examine the relationship between purchase volume and pricing to recommend strategies for cost-effective procurement.

- **Monitoring shipping efficiency**  
  Analyze freight cost distributions to identify logistics inefficiencies and negotiate better shipping arrangements.

- **Evaluating pricing strategies**  
  Use profit margins and sales trends to determine whether pricing adjustments are needed to stay competitive.

- **Forecasting demand**  
  Historical trends in turnover and sales are used to anticipate future demand and optimize inventory planning.

---

## 🚀 Features

- **Efficient Data Ingestion**  
  Reads CSV files in chunks to avoid memory overflow and enables smooth processing of datasets exceeding system capacity.

- **Vendor Summary Aggregation**  
  Combines data from multiple tables to compute metrics like gross profit, profit margin, stock turnover, and more.

- **Exploratory Data Analysis (EDA)**  
  Leverages Jupyter notebooks with visualizations and statistical techniques to uncover trends and validate business hypotheses.

- **Interactive Reporting with Power BI**  
  Enables stakeholders to explore vendor data through dashboards and filters without technical expertise.

- **Scalability and Performance**  
  Uses chunk-based processing, indexing, and optimized queries to handle datasets of 10M+ rows and beyond.

---

## 📂 Project Structure
```
Vendor-Performance-Data-Visualisation/
    ├── Data/ # Folder with raw CSV files
    ├── Logs/ # Folder for log files
    ├── vendor_summary.csv # Aggregated vendor metrics
    ├── vendor_sales_summary.csv # Detailed transactional data
    ├── Exploratory_Data_Analysis.ipynb # Notebook for data exploration
    ├── Vendor_Performance.ipynb # Notebook explaining data ingestion and flow
    ├── Vendor_Performance_Analysis.ipynb # Notebook with insights and analysis
    ├── Vendor Performance.pbix # Power BI dashboard
    ├── get_vendor_summary.py # Script to create summary tables
    ├── ingestion_db.py # Script for chunked data ingestion
    ├── README.md # This documentation file
```
---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SheikhNoor/Vendor-Performance-Data-Visualisation.git
   cd Vendor-Performance-Data-Visualisation
   ```
2. **Install required libraries:**
```bash
pip install pandas sqlalchemy matplotlib seaborn
```
3. **Prepare the dataset:**
Place your CSV files inside the `Data/` folder.

4. **Run the ingestion pipeline:**

```bash
Copy code
python ingestion_db.py
```
➤ Reads CSV files in chunks and populates the SQLite database.

5. **Generate vendor summaries:**

```bash
python get_vendor_summary.py
```
➤ Aggregates metrics across vendors and saves summary files.

6. **Explore the data:**
Launch Jupyter notebooks for analysis:

```bash
jupyter notebook Exploratory_Data_Analysis.ipynb
jupyter notebook Vendor_Performance.ipynb
jupyter notebook Vendor_Performance_Analysis.ipynb
```

---

## 📊 Key Metrics
```
| Metric                      | Formula                                      | Example                                                |
| --------------------------- | -------------------------------------------- | ------------------------------------------------------ |
| **Gross Profit**            | `TotalSalesDollars - TotalPurchaseDollars`   | If sales = 15000 and purchases = 12000 → profit = 3000 |
| **Profit Margin**           | `(GrossProfit / TotalSalesDollars) * 100`    | Profit = 3000, Sales = 15000 → margin = 20%            |
| **Stock Turnover**          | `TotalSalesQuantity / TotalPurchaseQuantity` | Sales = 200, Purchases = 100 → turnover = 2.0          |
| **Sales to Purchase Ratio** | `TotalSalesDollars / TotalPurchaseDollars`   | Sales = 15000, Purchases = 12000 → ratio = 1.25        |
```

---

## 📈 Insights
- Vendors with negative gross profits highlight pricing issues or unsustainable operations.
- Low stock turnover indicates slow-moving inventory, increasing holding costs.
- Bulk purchases significantly reduce unit costs, improving margins and cash flow.
- Weak correlations between pricing and profitability reveal external influences on vendor performance.
- Freight cost anomalies suggest irregular shipping patterns requiring negotiation.
- Confidence intervals reveal that low-performing vendors maintain higher margins, possibly due to premium offerings.

---

## 📂 Logging

Logs are saved in the `Logs/` folder, tracking:
- Data ingestion processes
- Errors and exceptions
- Timestamped operations for debugging and monitoring
This ensures fault tolerance and process transparency.

---

## 📂 Dataset Summary

- **Volume:** ~10 million rows across 4 tables
- **Challenge:** Memory management and processing efficiency
- **Solution:** Chunked ingestion, optimized SQL queries, and indexing
- **Applications:** Vendor selection, pricing optimization, supply chain management

---

## 📱 Connect with Me

Feel free to reach out or follow me on social media to stay updated with my work and projects:

- 💻 [GitHub](https://github.com/SheikhNoor) – Explore my code, projects, and contributions.
- 📧 [Email](mdnurullah.co@gmail.com) – Get in touch with me for collaboration or inquiries.
- 📸 [Instagram](https://www.instagram.com/im_snoah) – Follow my updates, photos, and stories.
- 💼 [LinkedIn](https://www.linkedin.com/in/md-nurullah-1481b7253) – Connect professionally and expand your network.


---

## 📜 License

This project is released under the MIT License, allowing you to modify and redistribute the code freely.

---

## 🚀 Future Enhancements

- Integrate with cloud services like AWS S3, Azure Blob Storage for scalable datasets
- Implement machine learning models for forecasting demand and detecting anomalies
- Create interactive dashboards with frameworks like Streamlit or Dash
- Expand dataset attributes to include customer feedback and vendor ratings
- Automate data pipelines with scheduling tools like Apache Airflow or Prefect
