from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# fastAPI is going to automatically validate the data based on the model of this class
class Post(BaseModel): # Post extends BaseModel
    title: str
    content: str
    published: bool = True # initialized variable
    rating: Optional[int] = None # initiliazed as none value

@app.get("/") # URL path
def read_root():
    return {"Welcome to my API!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(post: Post): # extract all of the fields from the body and convert to a python dictionary inside the varaible payLoad
    print(post)
    print(post.model_dump()) # convert to a dictionary
    return {"data": post}
