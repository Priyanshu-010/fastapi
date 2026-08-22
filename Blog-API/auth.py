from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import os
import dotenv

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#token create

def create_token(data: dict):
  to_encode = data.copy()

  expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

  to_encode.update({"exp": expire})

  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str= Depends(oauth2_schema)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  except JWTError:
    raise HTTPException(status_code=401, detail="Invalid Token")


# In this code the token is created and verified
# Code explanation step by step

# Step-1: Import the necessary modules
# Step-2: Define the secret key and algorithm
# Step-3: Define the access token expiration time
# Step-4: Define the create_token function
# Step-5: Define the verify_token function

# Explanation of the code
# We are using the jwt module to create and verify the token
# We are using the datetime module to get the current time
# We are using the timedelta module to get the access token expiration time
# We are using the HTTPException class to return the error message

