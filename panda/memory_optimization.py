import pandas as pd
import numpy as np


data = {
    "ID": np.arange(1, 11),                 
    "Age": np.random.randint(18, 60, 10),    
    "Salary": np.random.uniform(30000, 80000, 10) 
}

df = pd.DataFrame(data)
print("Before Optimization:\n", df.info(memory_usage="deep"))


df["ID"] = pd.to_numeric(df["ID"], downcast="unsigned")
df["Age"] = pd.to_numeric(df["Age"], downcast="unsigned")
df["Salary"] = pd.to_numeric(df["Salary"], downcast="float")

print("\nAfter Optimization:\n", df.info(memory_usage="deep"))
