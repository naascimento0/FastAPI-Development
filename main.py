from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/") # URL path
def read_root():
    return {"Welcome to my API!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)): # extract all of the fields from the body and convert to a python dictionary inside the varaible payLoad
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}
