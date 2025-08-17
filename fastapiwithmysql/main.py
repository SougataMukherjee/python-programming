from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

users = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"}
}

posts = {
    1: {"id": 1, "title": "First Post", "user_id": 1},
    2: {"id": 2, "title": "Second Post", "user_id": 2}
}

# ---------------- Pydantic Schemas ----------------
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

# ---------------- Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/",status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/posts/")
def create_post(post: PostBase, db: Session = Depends(get_db)):
    db_post = models.Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts[post_id]
