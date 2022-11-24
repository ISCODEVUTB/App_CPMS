from pymongo import MongoClient
import certifi


client = MongoClient(
    "mongodb+srv://david:TyuI1705$@cluster0.qqb9bkj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

db = client.wishlist_db


collection_name = db["wishlist_app"]
