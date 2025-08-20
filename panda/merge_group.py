import pandas as pd
from dataframe import df


dept = pd.DataFrame({
    "IsMarried": [True, False, True],
    "Department": ["HR", "IT", "Finance"]
})

#merge by column
merged = pd.merge(df, dept, on="IsMarried")
print("Merge by column:\n", merged)

#merge by index
merged_index = pd.concat([df, dept], axis=1)
print("\nMerge by index:\n", merged_index)