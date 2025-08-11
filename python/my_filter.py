numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print("even numbers",list(evens))

data = [0, 1, False, True, "", "hello", None]
truthy = filter(None, data)
print("remove falsy",list(truthy))