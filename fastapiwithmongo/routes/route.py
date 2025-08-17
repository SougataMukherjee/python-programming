# routes/route.py
from fastapi import APIRouter, HTTPException
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_todos():
    try:
        todos = list_serial(collection_name.find())
        return {"status": "success", "data": todos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching todos: {e}")


@router.post("/")
async def post_todo(todo: Todo):
    try:
        result = collection_name.insert_one(dict(todo))
        new_todo = collection_name.find_one({"_id": result.inserted_id})
        return {"status": "success", "data": individual_serial(new_todo)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting todo: {e}")


@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    try:
        updated_todo = collection_name.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": dict(todo)},
            return_document=True
        )
        if updated_todo:
            return {"status": "success", "data": individual_serial(updated_todo)}
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating todo: {e}")


@router.delete("/{id}")
async def delete_todo(id: str):
    try:
        deleted_todo = collection_name.find_one_and_delete({"_id": ObjectId(id)})
        if deleted_todo:
            return {"status": "success", "data": individual_serial(deleted_todo)}
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting todo: {e}")
