import requests
from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(requests.text, "html.parser")

# print(soup.title.text)


from fastapi import FastAPI

app = FastAPI()

@app.get("/news")
def get_news(page: int = 1, limit: int = 5):
  url = "https://news.ycombinator.com"

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  title = []

  for item in soup.find_all("span", class_="titleline"):
    title.append(item.text)

  # Pagination logic
  start = (page - 1) * limit
  end = start + limit

  return {
    "page": page,
    "limit": limit,
    "total": len(title),
    "data": title[start:end]
  }

# what is web crawling and pagination in web crawling:
# Web crawling is the process of extracting data from a website.
# Pagination is the process of dividing the data into pages.

# Explanation of Web crawling : 
# We are using the requests module to get the data from the website.
# We are using the BeautifulSoup module to parse the data.
# We are using the find_all method to get the data.
# We are using the page parameter to get the page number.
# We are using the limit parameter to get the limit.
# We are using the total parameter to get the total number of data.
# We are using the data parameter to get the data.


# We are using the page parameter to get the page number.
# We are using the limit parameter to get the limit.
# We are using the total parameter to get the total number of data.
# We are using the data parameter to get the data.