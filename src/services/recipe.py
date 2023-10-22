import uuid

from src.models.recipe import Recipe
from src.db.mongo_db import MongoClient
from src.config import settings


class RecipeService:

    # TODO: add annotation
    def __init__(self, database, collection_name):
        self.database = database
        self.collection_name = collection_name


    def _get_collection(self):
        return self.database.get_collection(self.collection_name)


    async def retrieve(self):
        print(self.database, self.collection_name)
        _recepie = []
        collection = self._get_collection().find()
        async for recipe in collection:
            _recepie.append(recipe)
        return _recepie


    async def insert(self, recepie: Recipe):
        _recepie = Recipe.model_dump(recepie)
        _recepie["_id"] = str(uuid.uuid4())
        result = await self._get_collection().insert_one(_recepie)
        return result.inserted_id


    async def update(self, id: str, recepie: Recipe):
        _recepie = await self._get_collection().find_one({"_id": id})
        _recepie["title"] = recepie.title
        _recepie["ingredients"] = recepie.ingredients
        _recepie["description"] = recepie.description
        await self._get_collection().update_one({"_id": id}, {"$set": _recepie})


    async def retrieve_id(self, id: str):
        return await self._get_collection().find_one({"_id": id})


    async def delete(self, id: str):
        await self._get_collection().delete_one({"_id": id})

def recipe_collection_dependency():
    recipe_service = RecipeService(database=MongoClient.get_db(), collection_name=settings.recipe_collection)

    yield recipe_service

