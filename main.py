from fastapi import FastAPI
from pydantic import BaseModel, create_model
from fastapi.exceptions import HTTPException

app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    description: str


class UpdatePost(BaseModel):
    title: str
    description: str


posts = []

@app.get("/test")
def test():
    return {"tittle":"Hey MAN"}

@app.post("/post")
def create_post(post:Post):
    posts.append(post.dict())
    return posts[-1]


@app.get("/posts")
def get_post():
    return posts

 
@app.get("/post/{id}")
def post_by_id(id: int):
    for item in posts:
        if item["id"] == id:
            return item
    raise HTTPException(404, detail="Page Not Found")    

@app.put("/post/{id}")
def update_post(id: int,post: UpdatePost):   
    for item in posts:
        if item['id'] == id:
            item['title'] = post.title
            item['description'] = post.description
            return item
    raise HTTPException(404, detail="Page Not Found")

@app.delete("/post/{id}")
def delete_by_post(id: int):
    for item in posts:
        if item["id"]== id:
            posts.remove(item)
            return {"message":"Post Deleted Successfully"}
    raise HTTPException(404, detail="Page Not Found")