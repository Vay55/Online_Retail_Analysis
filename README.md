# Online Retail Data QA & Warehouse Validation Project

## Overview

This project simulates a real-world data quality assurance and warehouse validation workflow using an online retail dataset from Kaggle.

The goal of the project was to investigate data quality issues, validate business rules, clean transactional retail data, and perform source-to-target warehouse validation using Python, Pandas, SQL, and SQLite.

The project focuses on the type of responsibilities commonly found in Data QA, Data Engineering, and Analytics Engineering roles.

---

# Tech stack

- Python
-- Pandas
-- SQLite
- SQL
- CSV Data Processing

---

# Project Structure

```text
online-retail/
│
├── raw_data/
│   └── OnlineRetail.csv
│
├── cleaned_retail.csv
├── warehouse.db
│
├── data_inspection.py
├── load_to_sql.py
├── sql_qa_checks.py
├── source_target_validation.py
│
└── README.md
```

---

# Project Workflow

## 1. Data Ingestion & Inspection

The raw retail dataset was loaded into Pandas for initial inspection and profiling.

Initial checks included:
- dataset structure inspection
- column validation
- datatype inspection
- null value detection
- duplicate row detection
- descriptive statistics analysis

### Example Findings

- 135,080 missing `CustomerID` values
- 5,268 duplicate rows
- negative quantities
- negative unit prices
- extreme outlier transactions

---

# 2. Anomaly Investigation

Several suspicious transaction patterns were investigated to determine whether they represented valid business activity or potential data quality issues.

## Cancellation Pattern Discovery

A business rule was identified where invoices beginning with `"C"` consistently contained negative quantities, indicating cancelled or returned transactions.

### Example

```text
InvoiceNo: C536391
Quantity: -24
```

SQL and Pandas validation checks confirmed that cancellation invoices did not contain positive quantities.

---

## Suspicious Anomaly Records

Additional anomalous records were discovered containing:
- missing product descriptions
- missing customer IDs
- zero unit prices
- negative quantities
- sequential invoice numbers

These records were categorized as likely internal adjustment or system-generated anomaly records.

### Findings

- 1,336 invalid negative quantity rows
- 862 high-confidence suspicious anomaly rows

---

# 3. Data Cleaning

A cleaning pipeline was implemented to prepare warehouse-ready data.

## Cleaning Steps

- removed duplicate rows
- removed rows with null descriptions
- removed highly suspicious anomaly records
- recalculated transaction totals

### Dataset Reduction

```text
541,909 rows → 535,187 rows
```

---

# 4. Warehouse Loading

The cleaned dataset was loaded into a SQLite database to simulate a warehouse fact table.

## Table Created

```sql
fact_sales
```

This stage simulated a simplified ETL warehouse loading workflow.

---

# 5. SQL QA Validation

SQL validation queries were written to perform warehouse integrity checks.

## Validation Checks

- total row validation
- null value validation
- negative price detection
- duplicate invoice investigation
- cancellation rule validation

### QA Rule

```sql
invalid_cancellations = df[
    df["InvoiceNo"].str.startswith("C")
    &
    (df["Quantity"] > 0)
]
```

### Validation Result

```text
0 invalid cancellation records found
```

---

# 6. Source-to-Target Validation

A source-to-target validation process was implemented to compare the raw dataset against the cleaned warehouse dataset.

## Validation Results

```text
Source rows: 541909
Target rows: 535187
Rows removed: 6722

Source duplicates: 5268
Target duplicates: 0

Source null descriptions: 1454
Target null descriptions: 0
```

This confirmed that:
- duplicate removal was successful
- null description cleaning was successful
- ETL transformations behaved as expected

---

# Key Skills Demonstrated

- Data Quality Assurance (QA)
- Data Validation
- ETL Concepts
- Source-to-Target Validation
- SQL QA Checks
- Data Cleaning
- Anomaly Detection
- Pandas Data Processing
- SQLite Warehouse Simulation
- Business Rule Validation

---

# Future Improvements

Possible future enhancements include:
- automated QA report generation
- Docker containerization
- PostgreSQL integration
- logging and monitoring
- Airflow/dbt pipeline integration
- dashboard visualization
- Kubernetes deployment simulation

---

# Dataset

Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/vijayuv/onlineretail?resource=download).
