from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Create instance
user = User(id=1, name="Alice", email="alice@example.com")
print(user)

# Validation example (this will throw an error if wrong type)
try:
    invalid_user = User(id="abc", name="Bob", email="bob@example.com")
except Exception as e:
    print("Validation error:", e)
