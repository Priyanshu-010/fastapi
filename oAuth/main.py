from fastapi import FastAPI, HTTPException, Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

# JWT Configuration
SECREY_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#OAuth Setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dummy User DB

fake_user_db = {
  "admin":{
    "username": "admin",
    "hashed_password": pwd_context.hash("1234"),
  }
}

# Hash Password
def hash_password(password: str):
  return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def create_token(data: dict):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  token = jwt.encode(to_encode, SECREY_KEY, algorithm=ALGORITHM)
  return token

# Login API (OAuth2 Form Token Generation)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm= Depends()):
  user = fake_user_db.get(form_data.username)
  if not user or not verify_password(form_data.password, user["hashed_password"]):
    raise HTTPException(status_code=401, detail="Invalid Credentials")

  access_token = create_token({"sub": form_data.username})
  return {"access_token": access_token, "token_type": "bearer"}

# Token Verify
def verify_token(token: str= Depends(oauth2_scheme)):
  try:
    payload = jwt.decode(token, SECREY_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
      raise HTTPException(status_code=401, detail="Invalid Token")
    return username
  except:
    raise HTTPException(status_code=401, detail="Invalid Token")  

# Protected Route

@app.get("/secure")
def secure_data(user= Depends(verify_token)):
  return {
    "message": f"Hello, {user}, you have access to this protected route",
    "user": user
  }