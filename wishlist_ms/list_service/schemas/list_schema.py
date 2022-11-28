def list_entity(list) -> dict:
    return {
        "id_client": list["id_client"],
        "items": [{
            "id_prod": list["items"][i]["id_prod"],
            "name":list["items"][i]["name"],
            "description":list["items"][i]["description"],
            "type_prod":list["items"][i]["type_prod"],
            "quantity":list["items"][i]["quantity"],
            "price":list["items"][i]["price"],
            "product_pic":list["items"][i]["product_pic"],

        }for i in range(len(list["items"]))],
    }


def lists_entity(lists) -> list:
    return [list_entity(wish_list) for wish_list in lists]
