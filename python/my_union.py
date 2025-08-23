from typing import Union

def square(x: Union[int,float])->float:
    return x*x

x=5
x=1.234
print(square(x))