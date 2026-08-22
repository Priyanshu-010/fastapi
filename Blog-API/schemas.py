# This file is like a types file in typescript

from pydantic import BaseModel


# Input Schema
class BlogCreate(BaseModel):
  title:str
  content:str

class BlogResponse(BaseModel):
  id: int
  title: str
  content: str

  class Config:
    from_attributes = True # This will convert the class to a dictionary
