age: int = 25
height: float = 5.9
is_student: bool = True

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("sam"),age,height)
