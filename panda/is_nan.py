import pandas as pd
import numpy as np

data = {
    "A": [1,2,np.nan,4,5],
    "B": [np.nan,2,3,4,5],
    "C": [1,np.nan,np.nan,4,5],
    "D": [1,np.nan,3,np.nan,5]
}
df=pd.DataFrame(data)
print(df)
print(df.isna())
print(df.isna().sum())
print(df.isna().any())
