import pandas as pd
import sqlite3

# LOAD CLEANED DATA

df = pd.read_csv(
    "cleaned_retail.csv",
    encoding="latin1"
)

# CREATE DATABASE CONNECTION

conn = sqlite3.connect("warehouse.db")

# LOAD DATA INTO SQL TABLE

df.to_sql(
    "fact_sales",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded into warehouse.db")