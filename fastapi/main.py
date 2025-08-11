from fastapi import FastAPI

# Create app instance
app = FastAPI()

# Root route


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

# Dynamic route


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
