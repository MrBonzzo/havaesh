from fastapi import FastAPI

from src.routers.recipe import router as recipe_router
from src.db.mongo_db import MongoClient


app = FastAPI()

app.add_event_handler("startup", MongoClient.init_db)
app.add_event_handler("shutdown", MongoClient.close_db)

app.include_router(recipe_router)


@app.get("/ping")
def ping():
    return {"message": "pong"}
