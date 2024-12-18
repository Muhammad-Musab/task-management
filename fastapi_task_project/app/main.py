from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .routes import users, tasks, templates
from .database import engine, Base

app = FastAPI()

# OAuth2 Bearer token scheme for extracting token from the request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Include the routers
app.include_router(users.router, prefix="/users")
app.include_router(tasks.router, prefix="/tasks")
app.include_router(templates.router, prefix="/templates")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Task Project"}
