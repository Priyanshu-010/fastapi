from fastapi import FastAPI, HTTPException, status, Depends, Header
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


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo):
  todos.append(todo)
  return {"message": "Todo Added", "data": todo}

@app.get("/todos/{id}")
def get_todo(id:int):
  for todo in todos:
    if todo.id == id:
      return todo
  # HTTPException is used to return an error response with a specific status code and detail message
  raise HTTPException(status_code=404, detail="Todo not found")

# With path, query, and request body parameters
@app.put("/todos/{id}")
def update_todo(id: int, updated_todo: Todo, notify: bool = False):
  for index, todo in enumerate(todos):
    if todo.id == id:
      todos[index] = updated_todo
      return {
        "message": "Todo updated",
        "data": updated_todo,
        "notify": notify
      }
  return {"error": "Todo not found"}


@app.delete("/todos/{id}")
def delete_todo(id: int):
  for index, todo in enumerate(todos):
    if todo.id == id:
      todos.pop(index)
      return {"message": "todo deleted"}

  return {"error": "Todo not found"}


# Dependency Injection in FastAPI with Depends  


# def common_logic():
#   return {"message": "This is a common logic function"}

# @app.get("/home")
# def home(data = Depends(common_logic)):
#   return data

# def get_current_user():
#   return {"user": "Priyanshu"}

# @app.get("/profile")
# def profile(user = Depends(get_current_user)):
#   return user

# @app.get("/dashboard")
# def dashboard(user = Depends(get_current_user)):
#   return user

# def verify_token(token: str = Header(None)):
#   if token != "mysecrettoken":
#     raise HTTPException(status_code=401, detail="Invalid Token")
#   return {
#     "user": "Authenticated User"
#   }

# @app.get("/secure-data")
# def secure_data(user = Depends(verify_token)):
#   return user