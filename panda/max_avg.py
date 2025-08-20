from dataframe import df

print(df.describe())        # Summary of all numeric columns
print(df["Age"].mean())  # Average salary
print(df["Age"].max())   # Max age