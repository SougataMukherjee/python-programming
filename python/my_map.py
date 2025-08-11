names = ["sam", "rupai", "sou"]
uppercase_names = map(str.upper, names)
print(list(uppercase_names))
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))
