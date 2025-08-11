def my_decorator(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"calling function: {func.__name__} with {arg}")
            result = func(*args, **kwargs)
            print(f" function: {func.__name__} completed")
            return result
        return wrapper
    return decorator


@my_decorator('sam')
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
