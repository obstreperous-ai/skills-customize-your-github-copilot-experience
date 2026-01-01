# FastAPI REST API Starter Code
# Install required packages: pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI application instance
app = FastAPI(title="My REST API", description="A simple REST API built with FastAPI")

# TODO: Define your Pydantic model here
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# In-memory storage (replace with database in production)
items = []


# TODO: Implement your endpoints here
# Example GET endpoint:
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API!"}


# TODO: Add GET endpoint to retrieve all items
# @app.get("/items", response_model=List[Item])
# def get_items():
#     pass


# TODO: Add POST endpoint to create a new item
# @app.post("/items", response_model=Item)
# def create_item(item: Item):
#     pass


# TODO: Add PUT endpoint to update an item
# @app.put("/items/{item_id}", response_model=Item)
# def update_item(item_id: int, item: Item):
#     pass


# TODO: Add DELETE endpoint to remove an item
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass


# Run the application with: uvicorn starter-code:app --reload
# Then visit http://localhost:8000/docs to see the API documentation
