from pydantic import BaseModel
from typing import Union, List


class Product(BaseModel):
    id_prod: int
    name: str
    description: str
    type_prod: str
    quantity: int
    price: int
    product_pic: str


class List(BaseModel):
    id_client: int
    items: Union[List[Product], None] = None
