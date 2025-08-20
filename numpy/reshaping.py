import numpy as np

arr = np.arange(12)  # [0,1,2,...,11]
print("Original Array:", arr)
print("Shape Array",arr.shape)

reshaped = arr.reshape(3, 4)
print("\nReshaped to 3x4:\n", reshaped)

flattened = reshaped.flatten()
print("\nFlattened Array:", flattened)
