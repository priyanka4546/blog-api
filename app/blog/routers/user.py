from fastapi import APIRouter, Depends
from app.blog import schemas, database
from sqlalchemy.orm import Session
from app.blog.repository import user

get_db= database.get_db
router=APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/',response_model=schemas.ShowUser )
def create_user(request: schemas.User,db:Session=Depends(get_db)):
    return user.create_user(db,request)

@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db) ):
    return user.get_user(id,db)