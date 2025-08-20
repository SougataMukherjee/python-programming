import pandas as pd


df = pd.read_excel("employees.xlsx",sheet_name="Sheet1")
print("Columns in Excel:", df.columns.tolist())
print("\nDataFrame Preview:")
print(df.head())
