from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()
DATABASE_URL = "sqlite:///test.db"

engine = create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
  db = sessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/")
def home(db: Session = Depends(get_db)):
  return {
    "message": "DB connected successfully"
  }

# what is sqlalchemy and all this stuff?
# It is a python library that is used to interact with databases.

# What is create_engine?
# It is a function that is used to create a connection to the database.

# What is sessionmaker?
# It is a function that is used to create a session object that is used to interact with the database.

# What is declarative_base?
# It is a class that is used to create a base class for all the models.

# What is Base?
# It is a base class that is used to create a table for all the models.

# What is sessionLocal?
# It is a session object that is used to interact with the database.

# Explantion of code and stuff line by line:

# We are using the FastAPI framework to build the API.
# We are using the create_engine function to create a connection to the database.
# We are using the sessionmaker function to create a session object that is used to interact with the database.
# We are using the declarative_base function to create a base class for all the models.
# We are using the Base class to create a table for all the models.
# We are using the sessionLocal function to create a session object that is used to interact with the database.