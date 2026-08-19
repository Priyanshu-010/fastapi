import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
async def home():
  await asyncio.sleep(3)
  return {"message": "Hello, World!"}


# def task():
#   time.sleep(3)
#   return "Hello"

# async def task():
#   await asyncio.sleep(3)
#   return "Hello"
