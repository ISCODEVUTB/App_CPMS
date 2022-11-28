from fastapi import APIRouter
from ..config.db import collection_name
from ..schemas.cart_schema import carts_entity
from ..schemas.product_schema import products_entity
from ..models.models import Cart, Product

cart = APIRouter()

# Constants
items_id_prod = 'items.id_prod'

# Get methods:

# Return a json of all the carts in the database.


@cart.get('/cart')
async def get_carts():
    carts = carts_entity(collection_name.find())
    return {"status": "ok", "data": carts}


# Return a json of the requested cart depending on the id.
@cart.get('/cart_client/{id_client}')
async def get_cart_client(id_client: int):
    cart = carts_entity(collection_name.find({'id_client': id_client}))
    return {"status": "ok", "data": cart}


# Post method:

# Insert a new cart in the database with the passed id.
@cart.post('/cart')
async def add_cart(id_client: int):
    cart = Cart(id_client=id_client, total=0, items=[])
    _id = collection_name.insert_one(dict(cart))
    cart = cart = carts_entity(collection_name.find({'_id': _id.inserted_id}))
    return {"status": "ok", "data": cart}


# Put methods:

# Add a product to a cart if already in the cart increase its quantity.
@cart.put('/cart/add_product/{id_client}')
async def add_product(id_client: int, product: Product):

    product_request = products_entity(collection_name.find({'id_client': id_client, items_id_prod: product.id_prod}, {
                                      "items": {"$elemMatch": {"id_prod": product.id_prod}}}))

    id_prod = product_request[0]['items'][0]['id_prod'] if product_request else 0

    if id_prod != 0:
        collection_name.update_many({'id_client': id_client, items_id_prod: id_prod}, {
                                    "$inc": {"items.$.cart_quantity": 1}}, upsert=True)
    else:
        collection_name.update_many({'id_client': id_client}, {
                                    "$push": {"items": dict(product)}}, upsert=True)

    cart_final = carts_entity(collection_name.find({'id_client': id_client}))
    return {"status": "ok", "data": cart_final}


# Remove product from the requested cart.
@cart.put('/cart/remove_product/{id_client}/{id_prod}')
async def remove_product(id_client: int, id_prod: int):

    collection_name.update_many({'id_client': id_client}, {
                                "$pull": {"items": {"id_prod": id_prod}}}, upsert=True)

    cart = carts_entity(collection_name.find({'id_client': id_client}))
    return {"status": "ok", "data": cart}


# Increase the quantity of a product in a cart.
@cart.put('/cart/increase_product/{id_client}/{id_prod}')
async def increase_product(id_client: int, id_prod: int):

    collection_name.update_many({'id_client': id_client, items_id_prod: id_prod}, {
                                "$inc": {"items.$.cart_quantity": 1}}, upsert=True)

    cart = carts_entity(collection_name.find({'id_client': id_client}))
    return {"status": "ok", "data": cart}


# Lessen the quantity of a product in a cart and if quantity=0 delete it.
@cart.put('/cart/decrease_product/{id_client}/{id_prod}')
async def decrease_product(id_client: int, id_prod: int):

    product_request = products_entity(collection_name.find(
        {'id_client': id_client, items_id_prod: id_prod}, {"items": {"$elemMatch": {"id_prod": id_prod}}}))

    cart_quantity = product_request[0]['items'][0]['cart_quantity'] if product_request else 0

    if cart_quantity <= 1:
        collection_name.update_many({'id_client': id_client}, {
                                    "$pull": {"items": {"id_prod": id_prod}}}, upsert=True)
    else:
        collection_name.update_many({'id_client': id_client, items_id_prod: id_prod}, {
                                    "$inc": {"items.$.cart_quantity": -1}}, upsert=True)

    cart_final = carts_entity(collection_name.find({'id_client': id_client}))
    return {"status": "ok", "data": cart_final}
