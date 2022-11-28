# Return a dictionary with the structure of the json. 
def provider_entity(provider) -> dict:
    return {
        "id": str(provider["_id"]),
        "name": provider["name"],
        "items": [{
            "id_prod": provider["items"][i]["id_prod"],
            "name":provider["items"][i]["name"],
            "description":provider["items"][i]["description"],
            "type_prod":provider["items"][i]["type_prod"],
            "quantity":provider["items"][i]["quantity"],
            "price":provider["items"][i]["price"],
        }for i in range(len(provider["items"]))],
    }

# Return a list of the dictionaries retrieved from the database.
def providers_entity(providers) -> list:
    return [provider_entity(provider) for provider in providers]
