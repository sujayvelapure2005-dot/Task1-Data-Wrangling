import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv", engine="python", encoding="latin1", on_bad_lines="skip")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nSummary statistics:")
print(df.describe())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.ffill()

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaning completed successfully!")