from typing import List
from fastapi import Depends, status, HTTPException, APIRouter
from .. database import get_db
from .. import models, schemas
from sqlalchemy.orm import Session
from .. utils import get_password_hash

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserRequest, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")

    new_user = models.User(
        name = user.name,
        email = user.email,
        password = get_password_hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

