from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import Settings
# import os
# from dotenv import load_dotenv

app = FastAPI()

# load_dotenv()

# Allowed origins (Front-end URL)
origin = [
  "YOUR FRONTEND URL" # Ex : http://localhost:3000
]

SECRET_KEY= Settings().SECRET_KEY
app.add_middleware(
  CORSMiddleware,
  allow_origins=origin, # Front-end URL
  allow_credentials=True, # Cookie Authentication
  allow_methods=["*"], # Get, Post, Put, Delete
  allow_headers=["*"] # Headers
)

@app.get("/")
def home():
  return {"message": f"Hello, World!, {SECRET_KEY}"}