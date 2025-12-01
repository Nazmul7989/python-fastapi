import uvicorn
from fastapi import FastAPI, Query, status
from typing import Optional, Annotated
from pydantic import BaseModel, Field

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

@app.get("/users", status_code=status.HTTP_200_OK, tags=["Users"])
def users(limit: int = 10, active: Optional[bool] = None):
    #Write logic to fetch users from database
    return {"data": f"Showing {limit} users", "active": active}

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK, tags=["Users"])
def read_user(user_id: int):
    #Write logic to fetch user from database
    return {"data": user_id}

#add multiple validation rule for name, like: string, min-2, max 100
class User(BaseModel):
   # name: str = Field(..., min_length=2, max_length=100)
    #name: Annotated[str, Field(min_length=2, max_length=100)]
    name: Annotated[str, Query(min_length=2, max_length=100)]
    age: int
    active: bool
    address: Optional[str] = None

    #add example data
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "age": 30,
                    "active": True,
                    "address": "123 Main St",
                }
            ]
        }
    }


@app.post("/users", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: User):
    #Write logic to create user in database
    return {"data": user}

@app.put("/users/{user_id}", tags=["Users"])
def update_user(user_id: int, user: User):
    #Write logic to update user in database
    return {"data": user}

@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    #Write logic to delete user from database
    return {"data": f"Deleted user id: {user_id}"}


# Custom host and port
# if __name__ == "__main__":
#     uvicorn.run(app, host= 'localhost', port=9000)








