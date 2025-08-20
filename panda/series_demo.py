import pandas as pd

s = pd.Series([10, 20, 30, 40, 50], name="Numbers")
print("Series Example:\n", s)

print("\nFirst element:", s[0])
print("Last element:", s.iloc[-1])

print("\nSeries multiplied by 2:\n", s * 2)
