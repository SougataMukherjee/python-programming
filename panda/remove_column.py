import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 28],
    "Score": [85, 90, 70, 88]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

#  Drop a column Score
df_no_score = df.drop(columns=["Score"])
print("\nAfter Dropping 'Score' Column:\n", df_no_score)

# Drop a row Charlie
df_no_charlie = df.drop(index=2)
print("\nAfter Dropping Row with index=2 (Charlie):\n", df_no_charlie)

# Drop multiple columns
df_multi_drop = df.drop(columns=["Age", "Score"])
print("\nAfter Dropping 'Age' and 'Score' Columns:\n", df_multi_drop)

# Drop multiple rows 
df_multi_row = df.drop(index=[0, 3])
print("\nAfter Dropping Rows with index=0 and 3 (Alice, David):\n", df_multi_row)
