from fastapi import FastAPI
from .routes.list_routes import wish_list

app = FastAPI()


app.include_router(wish_list)
