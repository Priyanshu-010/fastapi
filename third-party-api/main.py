import requests

# response =requests.get("https://jsonplaceholder.typicode.com/posts") # to get data based on on ID number we use https://jsonplaceholder.typicode.com/posts/1

# data = response.json()

# print(data[:2])


from fastapi import FastAPI, HTTPException

app = FastAPI()

# Get All data

@app.get("/posts")
def get_posts():
  url = "https://jsonplaceholder.typicode.com/posts"
  response = requests.get(url)
  if response.status_code == 200:
    raise HTTPException(status_code=404, detail="Data not found")

  return response.json

@app.get("/posts/{id}")
def get_post(id: int):
  url = f"https://jsonplaceholder.typicode.com/posts/{id}"
  response = requests.get(url)

  return response.json

