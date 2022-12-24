#import 
from fastapi import FastAPI 

#instance
app = FastAPI()

#Decorator
@app.get('/')

#function
def index():
    return {'data':{'name': 'Blog List'}}

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
