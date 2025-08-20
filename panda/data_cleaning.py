import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", None, "David"],
    "Age": [24, np.nan, 22, 30],
    "Score": [85, 90, None, 88]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


# Fill missing values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Score"].fillna(df["Score"].median(), inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

print("\nCleaned Data:\n", df)
