from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"message": "Hello, World!"}

@app.get("/about")
def about():
  return {"message": "This is a simple FastAPI application."}

@app.get("/add")
def add(a: int, b: int):
  return {"result": a + b}