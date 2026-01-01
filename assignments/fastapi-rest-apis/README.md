# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework, including endpoint creation, request handling, response models, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints that handle simple data operations.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Implement a GET endpoint at `/items/{item_id}` that returns item details
- Run the application using uvicorn and verify endpoints work


### 🛠️ Build a Simple CRUD API

#### Description
Create a REST API for managing a collection of items (e.g., books, tasks, or products) with full CRUD functionality.

#### Requirements
Completed program should:

- Define a Pydantic model for your item with at least 3 fields
- Implement POST endpoint to create new items
- Implement GET endpoint to retrieve all items
- Implement PUT endpoint to update an existing item by ID
- Implement DELETE endpoint to remove an item by ID
- Use an in-memory list to store items (database not required)
- Test all endpoints using the automatic API documentation at `/docs`
