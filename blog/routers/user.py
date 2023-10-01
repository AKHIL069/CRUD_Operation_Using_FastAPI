from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database
from sqlalchemy.orm import Session
from blog.repository import user



router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.post('/create', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db), status_code=200):
    return user.show(id, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), status_code=200):
    return user.delete(id, db)