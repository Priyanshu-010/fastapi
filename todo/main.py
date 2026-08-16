from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
  id: int
  title: str
  completed: bool

@app.get("/todos")
def get_todos():
  return todos


@app.post("/todos")
def create_todo(todo: Todo):
  todos.append(todo)
  return {"message": "Todo Added", "data": todo}

@app.get("/todos/{id}")
def get_todo(id:int):
  for todo in todos:
    if todo.id == id:
      return todo
  return {"error": "Todo not found"}

@app.put("/todos/{id}")
def update_todo(id: int, updated_todo: Todo):
  for index, todo in enumerate(todos):
    if todo.id == id:
      todos[index] = updated_todo
      return {
        "message": "Todo updated",
        "data": updated_todo
      }
  return {"error": "Todo not found"}


@app.delete("/todos/{id}")
def delete_todo(id: int):
  for index, todo in enumerate(todos):
    if todo.id == id:
      todos.pop(index)
      return {"message": "todo deleted"}

  return {"error": "Todo not found"}