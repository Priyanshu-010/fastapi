from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECREY_KEY = "mysecretkey"

ALGORITHM = "HS256"

def create_token(data: dict):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  token = jwt.encode(to_encode, SECREY_KEY, algorithm=ALGORITHM)
  return token

# Login API (Token Generation)

@app.post("/login")
def login(username:str, password: str):
  if username != "admin" or password != "admin":
    raise HTTPException(status_code=401, detail="Invalid Credentials")

  token = create_token({"sub": username})
  return {"token": token}

# Token Verify
def verify_token(token: str = Header(None)):
  try:
    payload = jwt.decode(token, SECREY_KEY, algorithms=[ALGORITHM])
    return payload
  except:
    raise HTTPException(status_code=401, detail="Invalid Token")


# Protected Route

@app.get("/secure")
def secure_data(user= Depends(verify_token)):
  return {"message": "Secure Data", "user": user}