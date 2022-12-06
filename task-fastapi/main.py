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
    return {'id': 0, 'timestamp': 0}

@app.get('/dog')
async def get_dogs(kind: DogType = None):
    if kind is not None:
        return [i for i in dogs if i['kind'] == kind]
    return dogs

@app.get('/dog/{pk}')
async def get_dog_by_pk(pk: int):
    for i in dogs:
        if i['pk'] == pk:
            return i
    raise HTTPException(status_code=404)

@app.post('/dog')
async def create_dog(dog: Dog):
    if dog.pk is not None:
        new_dog = OrderedDict([('pk', dog.pk), ('name', dog.name), ('kind', dog.kind)])
    else:
        new_dog = OrderedDict([('pk', len(dogs)), ('name', dog.name), ('kind', dog.kind)])
    dogs.append(new_dog)
    return new_dog

@app.patch('/dog/{pk}')
async def update_dog(pk: int, dog: Dog):
    for i in dogs:
        if i['pk'] == pk:
            dogs.remove(i)
            rd_dog = OrderedDict([('pk', pk), ('name', dog.name), ('kind', dog.kind)])
            dogs.append(rd_dog)
            return rd_dog
    raise HTTPException(status_code=404)

