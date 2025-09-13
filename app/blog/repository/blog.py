from sqlalchemy.orm import Session
from fastapi import HTTPException, status 
from app.blog import models, schemas


def get_all(db:Session):
   blogs=db.query(models.Blog).all()
   return blogs

def show(id,db:Session):
   blog=db.query(models.Blog).filter(models.Blog.id==id).first()
   if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id of {id} is not found ")
   return blog

def create(db:Session,request:schemas.Blog,current_user: models.User):
    new_blog=models.Blog(title=request.title, body=request.body,user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id). first()
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id of {id} is not found ")
    db.delete(blog)
    db.commit()
    return "deleted"

def update(id:int,db:Session,request:schemas.Blog,):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id of {id} is not found")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return "updated"