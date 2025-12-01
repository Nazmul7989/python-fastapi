from typing import List
from fastapi import Depends, status, HTTPException, APIRouter
from .. database import get_db
from .. import models, schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/categories", status_code=status.HTTP_200_OK, tags=["Categories"], response_model=List[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories

@router.get("/categories/{id}", status_code=status.HTTP_200_OK, tags=["Categories"], response_model=schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail= f"Category not found by id {id}")

    return category

@router.post('/categories', status_code=status.HTTP_201_CREATED, tags=["Categories"], response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryRequest, db: Session = Depends(get_db)):
    new_category = models.Category(
        name = category.name,
        description = category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return category

@router.put('/categories/{id}', status_code=status.HTTP_200_OK, tags=["Categories"], response_model=schemas.CategoryResponse)
def update_category(id: int, category: schemas.CategoryRequest, db: Session = Depends(get_db)):
    existing_category = db.query(models.Category).filter(models.Category.id == id).first()

    if not existing_category:
        raise HTTPException(status_code=404, detail= f"Category not found by id {id}")

    existing_category.name = category.name
    existing_category.description = category.description

    db.commit()
    db.refresh(existing_category)
    return existing_category


#Delete category
@router.delete('/categories/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Categories"])
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail= f"Category not found by id {id}")

    db.delete(category)
    db.commit()
    return {"data": "Category deleted successfully"}




