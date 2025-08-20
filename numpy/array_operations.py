import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Basic operations
print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Sum:", arr1.sum())
print("Max:", arr1.max())

# Scalar operations
print("Multiply by scalar:", arr1 * 10)

# 2d array
arr2D = np.array([[1, 2], [3, 4]])
print("shape and size",arr2D.shape,arr2D.size)
print("specific element",arr2D[0,1])
print("entire 1st col",arr2D[0:])
print("entire2nd row",arr2D[:1])

zeros = np.zeros((3, 3))             # 3x3 zeros
ones = np.ones((2, 2))               # 2x2 ones
print(zeros)
print(ones)
