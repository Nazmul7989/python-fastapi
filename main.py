import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"data": "Hello World"}

@app.get("/about")
def about():
    return {"data": "About Page"}

@app.get("/contact")
def contact():
    return {"data": "Contact Page"}

@app.get("/users")
def users(limit: int = 10, active: Optional[bool] = None):
    #Write logic to fetch users from database
    return {"data": f"Showing {limit} users", "active": active}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    #Write logic to fetch user from database
    return {"data": user_id}

class User(BaseModel):
    name: str
    age: int
    active: bool
    address: Optional[str] = None

@app.post("/users")
def create_user(user: User):
    #Write logic to create user in database
    return {"data": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    #Write logic to update user in database
    return {"data": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    #Write logic to delete user from database
    return {"data": f"Deleted user id: {user_id}"}


# Custom host and port
# if __name__ == "__main__":
#     uvicorn.run(app, host= 'localhost', port=9000)








