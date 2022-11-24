from fastapi import APIRouter
from ..config.db import collection_name
from ..schemas.cart_schema import cartsEntity
from ..models.models import Cart, Product

cart = APIRouter()



#get methods
@cart.get('/cart')
async def get_carts():
    carts = cartsEntity(collection_name.find())
    return {"status":"ok", "data": carts}


@cart.get('/cart_client/{id_client}')
async def get_cart_client(id_client: int):
    cart = cartsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": cart}


#post method
@cart.post('/cart')
async def add_cart(id_client:int):
    cart = Cart(id_client=id_client, total=0, items=[])
    _id = collection_name.insert_one(dict(cart))
    cart = cart = cartsEntity(collection_name.find({'_id':_id.inserted_id}))
    return {"status":"ok", "data": cart}


#put methods
@cart.put('/cart/add_product/{id_client}')
async def add_product(id_client:int, product: Product):
    
    id_prod = 0
    
    cart = cartsEntity(collection_name.find({'id_client':id_client}))
    for key, val in cart[0].items():
        if 'items' in key:
            for i in range(len(val)):
                for valor in val[i]:
                    if val[i]["id_prod"] == product.id_prod:
                        id_prod = val[i]["id_prod"]
                        break
    if id_prod == 0:
        collection_name.update_many({'id_client':id_client}, { "$push": {"items":dict(product)} }, upsert = True)
    else:
        collection_name.update_many({'id_client':id_client, 'items.id_prod':id_prod}, { "$inc": { "items.$.cart_quantity":1 } }, upsert = True)


    cart_final = cartsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": cart_final}


@cart.put('/cart/remove_product/{id_client}/{id_prod}')
async def remove_product(id_client:int, id_prod:int):

    collection_name.update_many({'id_client':id_client}, { "$pull": { "items":{ "id_prod":id_prod } } }, upsert = True)

    cart = cartsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": cart}


@cart.put('/cart/increase_product/{id_client}/{id_prod}')
async def increase_product(id_client:int, id_prod:int):

    collection_name.update_many({'id_client':id_client, 'items.id_prod':id_prod}, { "$inc": { "items.$.cart_quantity":1 } }, upsert = True)

    cart = cartsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": cart}


@cart.put('/cart/decrease_product/{id_client}/{id_prod}')
async def decrease_product(id_client:int, id_prod:int):

    cart_quantity = 0

    cart = cartsEntity(collection_name.find({'id_client':id_client}))
    for key, val in cart[0].items():
        if 'items' in key:
            for i in range(len(val)):
                for valor in val[i]:
                    if val[i]["id_prod"] == id_prod:
                        cart_quantity= val[i]["cart_quantity"]
                        break
    if cart_quantity <= 1:
        collection_name.update_many({'id_client':id_client}, { "$pull": { "items":{ "id_prod":id_prod } } }, upsert = True)
    else:
        collection_name.update_many({'id_client':id_client, 'items.id_prod':id_prod}, { "$inc": { "items.$.cart_quantity":-1 }  }, upsert = True)


    cart_final = cartsEntity(collection_name.find({'id_client':id_client}))
    return {"status":"ok", "data": cart_final}





