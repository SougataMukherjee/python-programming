import numpy as np

# Define a structured array with fields (name, age, marks)
student_dtype = np.dtype([("name", "U20"), ("age", "i4"), ("marks", "f4")])

students = np.array([
    ("Alice", 21, 85.5),
    ("Bob", 22, 90.0),
    ("Charlie", 20, 72.3)
], dtype=student_dtype)

print("Structured Array:")
print(students)

# Accessing fields
print("\nNames:", students["name"])
print("Ages:", students["age"])
print("Marks:", students["marks"])
