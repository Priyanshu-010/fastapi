import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import time

app = FastAPI()

# Cache Storage
cache_data = []
last_fetch = 0

@app.get("/news")
def get_news():
  global cache_data, last_fetch

  start = time.time()

  if time.time() - last_fetch > 60:
    print("Fetching fresh data...")
    url = "https://news.ycombinator.com"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
  
    cache_data =[
      item.text for item in soup.find_all("span", class_="titleline")
    ]

    last_fetch = time.time()

  else:
    print("Using cached data...")
  
  end = time.time()

  time_taken = round(end - start, 4)

  print("Time Taken", time_taken)

  return {
    "time_taken": time_taken,
    "data": cache_data[:5]
  }

# what is caching in FastAPI:
# Caching is the process of storing data in a temporary location to improve performance.
# FastAPI is a framework for building APIs.

# Explanation : 
# We are using a global variable to store the cached data and the last fetch time.
# We are using a decorator to cache the data.
# We are using the time module to get the current time.
# We are using the round function to round the time taken to 4 decimal places.
# Time is not necessary to be precise. It is just to show the time taken to fetch the data. we can ignore this.