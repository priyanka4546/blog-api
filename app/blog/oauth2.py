from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from typing import Annotated
from jose import jwt
from app.blog import models, database, token
from sqlalchemy.orm import Session
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
get_db = database.get_db

def get_current_user(token_str: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = token.verify_token(token_str, credentials_exception)
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user
  