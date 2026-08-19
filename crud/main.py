from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///test.db"

# Engine create (DB connection)
engine = create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread": False}
)

# Session (DB operations ke liye)
sessionLocal = sessionmaker(bind=engine)

# Base (model ke liye)
Base = declarative_base()


# Table (Model)
class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  completed = Column(String)


# Table create
Base.metadata.create_all(bind=engine)


# Dependency (DB session provide karega)
def get_db():
  db = sessionLocal()
  try:
    yield db
  finally:
    db.close()

# create todo
@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
  todo = Todo(title=title, completed="False")
  db.add(todo)
  db.commit()
  db.refresh(todo)
  return{
    "messaege": "Todo Created",
    "data": todo
  }

# get todos
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
  todos = db.query(Todo).all()
  return{
    "total": len(todos),
    "data": todos
  }

# get todo based on id
@app.get("/todos/{id}")
def get_todo(id: int, db: Session = Depends(get_db)):
  todo = db.query(Todo).filter(Todo.id == id).first()
  if not todo:
    raise HTTPException(status_code=404, detail="Todo not found")
  return todo

# update todo
@app.put("/todos/{id}")
def update_todo(id: int, title: str, db: Session = Depends(get_db)):
  todo = db.query(Todo).filter(Todo.id == id).first()
  if not todo:
      raise HTTPException(status_code=404, detail="Todo not found")

  todo.title = title
  db.commit()
  db.refresh(todo)
  return{
    "message": "Todo updated",
    "data": todo
  }

# delete todo
@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
  todo = db.query(Todo).filter(Todo.id == id).first()
  if not todo:
    raise HTTPException(status_code=404, detail="Todo not found")
  db.delete(todo)
  db.commit()
  return{
    "message": "Todo deleted"
  }