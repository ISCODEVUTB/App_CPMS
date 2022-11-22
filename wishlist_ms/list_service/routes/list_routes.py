from fastapi import APIRouter
from ..config.db import collection_name
from ..schemas.list_schema import listsEntity
from ..models.models import List, Product

wish_list = APIRouter()



#get methods
@wish_list.get('/wish_list')
async def get_list():
    lists = listsEntity(collection_name.find())
    return {"status":"ok", "data": lists}


@wish_list.get('/wish_list_client/{id_client}')
async def get_wish_list_client(id_client: int):
    wish_list = listsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": wish_list}


#post method
@wish_list.post('/wish_list')
async def add_list(id_client:int):
    wish_list = List(id_client=id_client, items=[])
    _id = collection_name.insert_one(dict(wish_list))
    wish_list = listsEntity(collection_name.find({'_id':_id.inserted_id}))
    return {"status":"ok", "data": wish_list}


#put methods
@wish_list.put('/wish_list/add_product/{id_client}')
async def add_product(id_client:int, product: Product):

    collection_name.update_many({'id_client':id_client}, { "$push": {"items":dict(product)} }, upsert = True)

    wish_list = listsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": wish_list}


@wish_list.put('/wish_list/remove_product/{id_client}/{id_prod}')
async def remove_product(id_client:int, id_prod:int):

    collection_name.update_many({'id_client':id_client}, { "$pull": { "items":{ "id_prod":id_prod } } }, upsert = True)

    wish_list = listsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": wish_list}






