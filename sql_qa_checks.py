import sqlite3
import pandas as pd

# CONNECT TO DATABASE

conn = sqlite3.connect("warehouse.db")

# 1. COUNT TOTAL ROWS

query1 = """
SELECT COUNT(*) AS total_rows
FROM fact_sales;
"""
print(pd.read_sql(query1, conn))

# 2. FIND NULL DESCRIPTIONS

query2 = """
SELECT COUNT(*) AS null_descriptions
FROM fact_sales
WHERE Description IS NULL;
"""

print(pd.read_sql(query2, conn))

# 3. FIND NEGATIVE PRICES

query3 = """
SELECT COUNT(*) AS negative_prices
FROM fact_sales
WHERE UnitPrice < 0;
"""

print(pd.read_sql(query3, conn))

# 4. FIND DUPLICATE INVOICES

query4 = """
SELECT InvoiceNo, COUNT(*) as duplicate_count
FROM fact_sales
GROUP BY InvoiceNo
HAVING COUNT(*) > 1
LIMIT 10;
"""

print(pd.read_sql(query4, conn))

# 5. CHECK CANCELLATION RULE

query5 = """
SELECT COUNT(*) AS invalid_cancellations
FROM fact_sales
WHERE InvoiceNo LIKE 'C%'
AND Quantity > 0;
"""

print(pd.read_sql(query5, conn))