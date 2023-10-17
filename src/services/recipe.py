import uuid

from src.models.recipe import Recipe
from src.db.mongo_db import database


class RecipeService:
    @staticmethod
    async def retrieve():
        _recepie = []
        collection = database.get_collection("recipes").find()
        async for recipe in collection:
            _recepie.append(recipe)
        return _recepie

    @staticmethod
    async def insert(recepie: Recipe):
        _recepie = Recipe.model_dump(recepie)
        _recepie["_id"] = str(uuid.uuid4())
        print(_recepie)
        result = await database.get_collection("recipes").insert_one(_recepie)
        print(result.inserted_id)

    @staticmethod
    async def update(id: str, recepie: Recipe):
        _recepie = await database.get_collection("recipes").find_one({"_id": id})
        _recepie["title"] = recepie.title
        _recepie["ingredients"] = recepie.ingredients
        _recepie["description"] = recepie.description
        await database.get_collection("recipes").update_one({"_id": id}, {"$set": _recepie})

    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection("recipes").find_one({"_id": id})

    @staticmethod
    async def delete(id: str):
        await database.get_collection("recipes").delete_one({"_id": id})
