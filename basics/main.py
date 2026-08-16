from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
  name: str
  age: int
  email: str

class Address(BaseModel):
  city: str
  pincode: int

class newUser(BaseModel):
  name:str
  age:int
  address: Address

@app.get("/")
def home():
  return {"message": "Hello, World!"}

@app.get("/about")
def about():
  return {"message": "This is a simple FastAPI application."}

@app.get("/users")
def users():
  return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/users/{user_id}")
def get_user(user_id: int):
  return {"user_id": user_id}

@app.get("/user")
def get_query(name: str = None):
  return {"name": name}

@app.get("/products")
def get_products(limit: int = 10):
  return {"limit": limit}

@app.get("/items")
def get_items(name: str = None, price: int = 0):
  return {"name": name, "price": price}

@app.post("/create_user")
def create_user(user:User):
  return {
    "message": "User created successfully",
    "data": user
  }

@app.post("/create_new_user")
def create_new_user(new_user: newUser):
  return {
    "message": "New user created successfully",
    "data": new_user
  }