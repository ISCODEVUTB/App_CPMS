from fastapi import APIRouter
from ..config.db import collection_name
from ..schemas.provider_schema import providersEntity
from ..models.models import Provider, Product
from bson import ObjectId


provider = APIRouter()


# Get methods:

# Return a json of all the providers in the database.
@provider.get('/providers')
async def get_providers():
    providers = providersEntity(collection_name.find())
    return {"status": "ok", "data": providers}


# Return a json of the requested provider depending on the id.
@provider.get('/provider/{id}')
async def get_provider_by_id(id: str):
    provider = providersEntity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Return a json of a product that belongs to the provider requestd.
@provider.get('/provider/{id}/{id_prod}')
async def get_provider_by_id_with_product(id: str, id_prod: int):
    provider = providersEntity(collection_name.find({'_id': ObjectId(id)}))

    for key, val in provider[0].items():
        if 'items' in key:
            for i in range(len(val)):
                for valor in val[i]:
                    if val[i]["id_prod"] == id_prod:
                        return {
                            "Name": val[i]["name"],
                            "Desc": val[i]['description'],
                            "Type": val[i]['type_prod'],
                            "Quantity": val[i]['quantity'],
                            "Price": val[i]['price'],
                            "Provider_id": id,
                            "Provider_id_prod": val[i]['id_prod']
                        }


# Post method:

# Insert a new provider in the database with the passed name.
@provider.post('/provider')
async def add_provider(name: str):
    providerObj = Provider(name=name, items=[])
    _id = collection_name.insert_one(dict(providerObj))
    provider = providersEntity(collection_name.find({'_id': _id.inserted_id}))
    return {"status": "ok", "data": provider}


# Put methods:

# Add a product to the requested provider.
@provider.put('/provider/add_product/{id}')
async def add_product_to_provider(id: str, id_prod: int, product_name: str, prod_description: str, type_product: str, prod_quantity: int, prod_price: int):
    product_ex = Product(id_prod=id_prod, name=product_name, description=prod_description,
                         type_prod=type_product, quantity=prod_quantity, price=prod_price)

    collection_name.update_many({'_id': ObjectId(id)}, {
                                "$push": {"items": dict(product_ex)}}, upsert=True)

    provider = providersEntity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Remove a product to the requested provider.
@provider.put('/provider/remove_product/{id}/{id_prod}')
async def remove_product_from_provider(id: str, id_prod: int):

    collection_name.update_many({'_id': ObjectId(id)}, {
                                "$pull": {"items": {"id_prod": id_prod}}}, upsert=True)

    provider = providersEntity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Update the requested provider name.
@provider.put('/provider/{id}')
async def change_name_provider(name: str, id: str):

    collection_name.find_one_and_update(
        {'_id': ObjectId(id)}, {"$set": {"name": name}})

    provider = providersEntity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Delete method:

# Delete the provider from the database and return the empty data.
@provider.delete('/provider_delete/{id}')
async def delete_provider(id: str):
    collection_name.find_one_and_delete({'_id': ObjectId(id)})

    return {"status": "ok", "data": []}
