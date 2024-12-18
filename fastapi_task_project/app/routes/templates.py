from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Template
from pydantic import BaseModel

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for Template creation
class TemplateCreate(BaseModel):
    name: str
    data: str  # Store JSON or data as a string

@router.post("/")
def create_template(template: TemplateCreate, db: Session = Depends(get_db)):
    db_template = Template(name=template.name, data=template.data)
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return {"message": "Template created successfully", "template": db_template}

@router.get("/{template_id}")
def get_template(template_id: int, db: Session = Depends(get_db)):
    db_template = db.query(Template).filter(Template.id == template_id).first()
    if db_template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return db_template
