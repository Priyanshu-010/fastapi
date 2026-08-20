from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed origins (Front-end URL)
origin = [
  "YOUR FRONTEND URL" # Ex : http://localhost:3000
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origin, # Front-end URL
  allow_credentials=True, # Cookie Authentication
  allow_methods=["*"], # Get, Post, Put, Delete
  allow_headers=["*"] # Headers
)

@app.get("/")
def home():
  return {"message": "Hello, World!"}