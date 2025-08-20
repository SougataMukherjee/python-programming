import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 28],
    "Score": [85, 90, 70, 88]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)


print("\nShape of DataFrame (rows, columns):", df.shape)


print("Number of rows:", df.shape[0])

print("Number of columns:", df.shape[1])
