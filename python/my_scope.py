# local, global, nonlocal
global x   # Global variable
x = 30


def outer():
    x = 20

    def inner():
        nonlocal x
        x = 10
        print("Inner:", x)
    inner()
    print("Outer:", x)


outer()
print("Global:", x)
