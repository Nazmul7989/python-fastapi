from datetime import timedelta, datetime, timezone
from fastapi import APIRouter, status
from .. import schemas, models, oauth2
from .. database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from .. utils import verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.LoginResponse)
def login(user: schemas.LoginRequest, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email does not exists")

    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")


    #Create access token
    access_token_expires = timedelta(minutes=oauth2.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = oauth2.create_access_token(
        data={"email": user.email},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# @router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.LoginResponse)
# def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     existing_user = db.query(models.User).filter(models.User.email == user.username).first()
#     if not existing_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email does not exists")
#
#     if not verify_password(user.password, existing_user.password):
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
#
#
#     #Create access token
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"email": user.email},
#         expires_delta=access_token_expires
#     )
#
#     return {
#         "access_token": access_token,
#         "token_type": "bearer"
#     }

