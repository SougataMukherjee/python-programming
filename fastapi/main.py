from fastapi import FastAPI
from pydantic import BaseModel #like typescript in python
from typing import List

app = FastAPI()

# Pydantic Model
class Model(BaseModel):
    id: int
    name: str
    origin: str

# In-memory storage
models: List[Model] = [
    Model(id=1, name="Model A", origin="India"),
    Model(id=2, name="Model B", origin="Japan"),
    Model(id=3, name="Model C", origin="Germany"),
]

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

# Get all models
@app.get("/model", response_model=List[Model])
def get_models():
    return models

# Add a new model
@app.post("/model", response_model=Model)
def add_model(model: Model):
    models.append(model)
    return model

# Update an existing model
@app.put("/model/{model_id}", response_model=Model)
def update_model(model_id: int, updated_model: Model):
    for index, item in enumerate(models):
        if item.id == model_id:
            models[index] = updated_model
            return updated_model
    return {"error": "Model not found"}

# Delete a model
@app.delete("/model/{model_id}")
def delete_model(model_id: int):
    for index, item in enumerate(models):
        if item.id == model_id:
            deleted = models.pop(index)
            return {"message": "Model deleted", "deleted": deleted}
    return {"error": "Model not found"}
