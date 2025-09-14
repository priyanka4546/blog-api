from fastapi import FastAPI
from app.blog import models
from app.blog.database import engine
from app.blog.routers import blog, user, authentication
import uvicorn
import os

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

@app.get("/")
def greet():
    return "Welcome"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)



