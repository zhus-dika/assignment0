from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Header, HTTPException
from enum import Enum

app = FastAPI()
class DogType(str, Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'

class Dog(BaseModel):
    name: str
    pk: Union[int, None] = None
    kind: DogType

@app.get('/')
async def root():
    return {'message': 'Hello world'}

@app.post('/post')
async def get_post():
    return {'id': 0,
            'timestamp': 0
             }
@app.get('/dog')
async def get_dogs(kind: DogType = None):
    dogs = []
    if kind == None:
        kind = DogType.dalmatian
    dog = Dog(name = 'dika', kind = kind, pk = 0)
    dogs.append(dog)
    return [dog]

@app.get('/dog/{pk}')
async def get_dog_by_pk(pk: int):
    dog = Dog(name = 'dika', kind = DogType.dalmatian, pk = pk)
    return dog

@app.post('/dog')
async def create_dog(dog: Dog):
    return dog

@app.patch('/dog/{pk}')
async def update_dog(pk: int, dog: Dog):
    dog.pk = pk
    return dog
