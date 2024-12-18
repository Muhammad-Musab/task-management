

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Task as DBTask  # SQLAlchemy Task model
from app.schemas import TaskCreate, Task  # Pydantic TaskCreate and Task models
from app.utils.security import get_current_user
from app.models import User  # Assuming User model is imported here

router = APIRouter()

# Create a task by the authenticated user
@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Add the user_id to the task creation (assuming the Task model has a user_id field)
    db_task = DBTask(
        title=task.title,
        short_description=task.short_description,
        description=task.description,
        user_id=current_user.id  # Assuming the User model has an id field
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks of the authenticated user
@router.get("/", response_model=list[Task])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = db.query(DBTask).filter(DBTask.user_id == current_user.id).all()  # Filter by current user's ID
    return tasks
