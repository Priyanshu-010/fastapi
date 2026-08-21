from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

limiter = Limiter(key_func=get_remote_address) # this tracks the ip address of every request and user
app.state.limiter = limiter

# Error handling
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
  return JSONResponse(
    status_code=429,
    content={
      "detail": "Too Many Requests",
    }
  )

# Rate Limiter API

@app.get("/data")
@limiter.limit("3/minute")
def get_data(request: Request):
  return {"message": "Data"}  

# What is rate limit in FastAPI:
# Rate limit is the process of limiting the number of requests that can be made to a server or a service.
# FastAPI is a framework for building APIs.

# Explanation of the code and stuff:
# We are using the FastAPI framework to build the API.
# We are using the Limiter class to limit the number of requests that can be made to the API.
# We are using the get_remote_address function to get the IP address of the client.
# We are using the RateLimitExceeded class to handle the rate limit exceeded error.
# We are using the JSONResponse class to return the error message.