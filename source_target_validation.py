import pandas as pd

# LOAD SOURCE DATA

source_df = pd.read_csv(
    "raw_data/OnlineRetail.csv",
    encoding="latin1"
)

# LOAD TARGET DATA

target_df = pd.read_csv(
    "cleaned_retail.csv",
    encoding="latin1"
)

# SOURCE METRICS

source_rows = len(source_df)
source_duplicates = source_df.duplicated().sum()
source_null_descriptions = (
    source_df["Description"].isnull().sum()
)

# TARGET METRICS

target_rows = len(target_df)
target_duplicates = target_df.duplicated().sum()
target_null_descriptions = (
    target_df["Description"].isnull().sum()
)

# VALIDATION RESULTS

rows_removed = source_rows - target_rows

print("\nSOURCE TO TARGET VALIDATION")
print("============================")

print(f"Source rows: {source_rows}")
print(f"Target rows: {target_rows}")
print(f"Rows removed: {rows_removed}")

print("\nDUPLICATE VALIDATION")
print("====================")

print(f"Source duplicates: {source_duplicates}")
print(f"Target duplicates: {target_duplicates}")

print("\nNULL DESCRIPTION VALIDATION")
print("===========================")

print(
    f"Source null descriptions: "
    f"{source_null_descriptions}"
)

print(
    f"Target null descriptions: "
    f"{target_null_descriptions}"
)

# BASIC VALIDATION STATUS

if target_duplicates == 0:
    print("\nDuplicate removal successful.")

if target_null_descriptions == 0:
    print("Null description cleaning successful.")