from typing import TypedDict,Dict

class Movie(TypedDict):
    name:str
    year:int

movie=Movie(name="Avengers",year=2019)
print('movie: ', movie)