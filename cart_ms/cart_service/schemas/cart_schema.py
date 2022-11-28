def cart_entity(cart) -> dict:
    """Return a dictionary

    Json structure for the Cart object that'll be used within the app.
    """
    return {
        "id_client": cart["id_client"],
        "total": sum([cart["items"][i]["cart_quantity"] * cart["items"][i]["price"] for i in range(len(cart["items"]))]),
        "items": [{
            "id_prod": cart["items"][i]["id_prod"],
            "name":cart["items"][i]["name"],
            "description":cart["items"][i]["description"],
            "type_prod":cart["items"][i]["type_prod"],
            "quantity":cart["items"][i]["quantity"],
            "price":cart["items"][i]["price"],
            "product_pic":cart["items"][i]["product_pic"],
            "cart_quantity":cart["items"][i]["cart_quantity"],
            "total_item":cart["items"][i]["cart_quantity"] * cart["items"][i]["price"],
        }for i in range(len(cart["items"]))],
    }


def carts_entity(carts) -> list:
    """Return a list

    List of the dictionaries retrieved from the data base.
    """
    return [cart_entity(cart) for cart in carts]
