import pandas as pd

# simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 18],
    "IsMarried": [True, False, True]
}

df = pd.DataFrame(data)

print("Our DataFrame:")
print(df)

print("\nAverage Age:", df["Age"].mean())
