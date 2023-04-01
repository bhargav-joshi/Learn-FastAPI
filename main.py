#import 
from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel
import uvicorn

#instance
app = FastAPI()

#Decorator
@app.get('/blog')
#function
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}

#Dynamic Routing : remember the data types
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    #fetch blog id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    # return request
    return {'data' : f"Blog Created with title{request.title}"}




# Debugging Purpose
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port= 9000)