from fastapi import APIRouter
from ..config.db import collection_name
from ..schemas.provider_schema import providers_entity
from ..models.models import Provider, Product
from bson import ObjectId


provider = APIRouter()


# Get methods:

# Return a json of all the providers in the database.
@provider.get('/providers')
async def get_providers():
    providers = providers_entity(collection_name.find())
    return {"status": "ok", "data": providers}


# Return a json of the requested provider depending on the id.
@provider.get('/provider/{id}')
async def get_provider_by_id(id: str):
    provider = providers_entity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Return a json of a product that belongs to the provider requestd.
@provider.get('/provider/{id}/{id_prod}')
async def get_provider_by_id_with_product(id: str, id_prod: int):
    provider = providers_entity(collection_name.find({'_id': ObjectId(id)}))

    print(provider)

    for product in provider[0]['items']:
        if product["id_prod"] == id_prod:
            return {
                "Name":product["name"],
                "Desc":product['description'],
                "Type":product['type_prod'],
                "Quantity":product['quantity'],
                "Price":product['price'],
                "Provider_id": id,
                "Provider_id_prod":product['id_prod']
            }


# Post method:

# Insert a new provider in the database with the passed name.
@provider.post('/provider')
async def add_provider(name: str):
    provider_obj = Provider(name=name, items=[])
    _id = collection_name.insert_one(dict(provider_obj))
    provider = providers_entity(collection_name.find({'_id': _id.inserted_id}))
    return {"status": "ok", "data": provider}


# Put methods:

# Add a product to the requested provider.
@provider.put('/provider/add_product/{id}')
async def add_product_to_provider(id: str, id_prod: int, product_name: str, prod_description: str, type_product: str, prod_quantity: int, prod_price: int):
    product_ex = Product(id_prod=id_prod, name=product_name, description=prod_description,
                         type_prod=type_product, quantity=prod_quantity, price=prod_price)

    collection_name.update_many({'_id': ObjectId(id)}, {
                                "$push": {"items": dict(product_ex)}}, upsert=True)

    provider = providers_entity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Remove a product to the requested provider.
@provider.put('/provider/remove_product/{id}/{id_prod}')
async def remove_product_from_provider(id: str, id_prod: int):

    collection_name.update_many({'_id': ObjectId(id)}, {
                                "$pull": {"items": {"id_prod": id_prod}}}, upsert=True)

    provider = providers_entity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Update the requested provider name.
@provider.put('/provider/{id}')
async def change_name_provider(name: str, id: str):

    collection_name.find_one_and_update(
        {'_id': ObjectId(id)}, {"$set": {"name": name}})

    provider = providers_entity(collection_name.find({'_id': ObjectId(id)}))
    return {"status": "ok", "data": provider}


# Delete method:

# Delete the provider from the database and return the empty data.
@provider.delete('/provider_delete/{id}')
async def delete_provider(id: str):
    collection_name.find_one_and_delete({'_id': ObjectId(id)})

    return {"status": "ok", "data": []}
