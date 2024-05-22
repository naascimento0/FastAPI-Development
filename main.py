from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# fastAPI is going to automatically validate the data based on the model of this class
class Post(BaseModel): # Post extends BaseModel
    title: str
    content: str
    published: bool = True # initialized variable
    rating: Optional[int] = None # initiliazed as none value

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite_foods", "content": "I like pizza", "id": 2}]

@app.get("/") # URL path
def read_root():
    return {"Welcome to my API!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post): # extract all of the fields from the body and convert to a python dictionary inside the varaible payLoad
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
