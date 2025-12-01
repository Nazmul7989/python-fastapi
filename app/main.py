from fastapi import FastAPI
from . database import engine
from . import models
from . routers import category, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", tags=['Home'])
def index():
    return {"data": "Home Page"}

app.include_router(category.router)
app.include_router(user.router)











