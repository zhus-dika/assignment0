from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from enum import Enum

from pydantic.utils import OrderedDict

dogs = []
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
    return 'ok'

@app.post('/post')
async def get_post():
    return {'id': 0,
            'timestamp': 0
             }
@app.get('/dog')
async def get_dogs():
    return dogs

@app.get('/dog/{pk}')
async def get_dog_by_pk(pk: int):
    for i in dogs:
        if i['pk'] == pk:
            return i
    raise HTTPException(status_code=404)

@app.post('/dog')
async def create_dog(dog: Dog):
    new_dog = OrderedDict([('pk', dog.pk), ('name', dog.name), ('kind', dog.kind)])
    dogs.append(new_dog)
    return dog

@app.patch('/dog/{pk}')
async def update_dog(pk: int, dog: Dog):
    for i in dogs:
        if i['pk'] == pk:
            dogs.remove(i)
            dog.pk = pk
            dogs.append(dog)
            return dog
    raise HTTPException(status_code=404)
