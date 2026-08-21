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


# What is async await and asyncio in Python?
# Asyncio is a library that allows you to write asynchronous code in Python. It provides a way to write code that can run concurrently, without blocking the main thread.