from dataframe import df

print(df["Name"])

# Select multiple columns
print(df[["Name", "Age"]])

# Select rows by condition
print(df[df["Age"] > 25])