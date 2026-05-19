import pandas as pd

df = pd.read_csv(
    "raw_data/OnlineRetail.csv",
    encoding="latin1"
                 )

print(df.head())
print(df.columns)
print(df.info())


print(df.isnull().sum())
print(df.describe())
print(df.duplicated().sum())


#total revenue
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print(df[["Quantity", "UnitPrice", "TotalPrice"]].head())

#negative quantities
print(df[df["Quantity"] < 0].head(10))

#negative prices
print(df[df["UnitPrice"] < 0].head())

#missing customer IDs
print(df[df["CustomerID"].isnull()].head())

#checking if "C" means cancellation
print(df[df["InvoiceNo"].str.startswith("C")].head())
print(df[df["InvoiceNo"].str.startswith("C")]["Quantity"].describe())


print(
    df[df["Quantity"] == -80995]
)

# QA RULE:
# Cancellation invoices should have negative quantities
cancelled_orders = df["InvoiceNo"].str.startswith("C")

invalid_cancellations = df[
    cancelled_orders & (df["Quantity"] > 0)
]

print(invalid_cancellations)


# Orders invoices should have positive quantities
normal_orders = ~df["InvoiceNo"].str.startswith("C")

invalid_negative_quantities = df[
    normal_orders & (df["Quantity"] < 0)
]

print(invalid_negative_quantities.head())


#invalid rows
print(
    "Invalid negative quantity rows:",
    len(invalid_negative_quantities)
)

#might be internal company records and not customer purchases
print(
    invalid_negative_quantities[
        [
            "InvoiceNo",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID"
        ]
    ].head(20)
)


#anomaly category
anomaly_rows = invalid_negative_quantities[
    invalid_negative_quantities["Description"].isnull()
    &
    (invalid_negative_quantities["UnitPrice"] == 0)
]

print("Suspicious anomaly rows:", len(anomaly_rows))




print("\nQA SUMMARY")
print("===========")

print("Duplicate rows:", df.duplicated().sum())

print(
    "Missing Customer IDs:",
    df["CustomerID"].isnull().sum()
)

print(
    "Negative prices:",
    len(df[df["UnitPrice"] < 0])
)

print(
    "Invalid negative quantity rows:",
    len(invalid_negative_quantities)
)






#Data Cleaning

clean_df = df.copy()

clean_df = clean_df.drop_duplicates()

clean_df = clean_df[
    ~(
        clean_df["Description"].isnull()
        &
        (clean_df["UnitPrice"] == 0)
        &
        (clean_df["Quantity"] < 0)
    )
]

clean_df = clean_df[
    clean_df["Description"].notnull()
]

clean_df.to_csv(
    "cleaned_retail.csv",
    index=False
)