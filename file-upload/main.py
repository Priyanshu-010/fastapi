from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

# Might be without virtual environment so run with ucivorn without virtual environment and if not worked then try with virtual environment

app = FastAPI()

# STEP-1: Ensure uploads folder exists

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
  os.makedirs(UPLOAD_DIR)

# STEP-2 Static file setup

app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

# STEP-3 File Upload api
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
  filename = file.filename
  file_path = os.path.join(UPLOAD_DIR, filename)

  if not filename:
    raise HTTPException(status_code=400, detail="No file uploaded")

  with open(file_path, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

  return {
    "message": "File uploaded successfully",
    "filename": filename,
    "file_url": f"http://127.0.0.1:8000/files/{filename}"
  }

# STEP_4 Get File URL API
@app.get("/files/{filename}")
def get_file(filename:str):
  file_path = os.path.join(UPLOAD_DIR, filename)

  if not os.path.exists(file_path):
    raise HTTPException(status_code=404, detail="File not found")

  return {"file_url": f"http://127.0.0.1:8000/files/{filename}"}

@app.get("/")
def home():
  return {"message": "Hello, World!"}

# Code Explanation step by step

# Step-1: Ensure uploads folder exists
# Step-2: Static file setup
# Step-3: File Upload api
# Step-4: Get File URL API

# Explanation of the code
# We are using the FastAPI framework to build the API.
# We are using the UploadFile class to get the file from the request.
# We are using the File class to get the file from the request.
# We are using the HTTPException class to return the error message.
# We are using the os module to get the file path.
# We are using the shutil module to copy the file to the uploads folder.
# We are using the os module to get the file path.
# We are using the os module to get the file path.
# We are using the os module to get the file path.
