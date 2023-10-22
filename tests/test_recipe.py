import pytest
import asyncio
from fastapi.testclient import TestClient

from src.app import app
from src.models.recipe import Recipe, Ingredient
# from src.services.recipe import RecipeService, get_recipe_service
from src.db.mongo_db import client as db_client

# client = TestClient(app)

# class TestRecipeService(RecipeService):
#     database=db_client.test_database



# app.dependency_overrides[get_recipe_service] = TestRecipeService


def test_create_and_get():
    client = TestClient(app)
    test_recipe_1 = Recipe(title="Рецепт 1", ingredients=[Ingredient(name="Ингредиент_1").model_dump()], description="Описание 1").model_dump()
    response = client.post("/recipe/create", json=test_recipe_1)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("message") == "Success save data"
    client = TestClient(app)
    response = client.get("/recipe")
    assert response.status_code == 200
    assert len(response_json.get("result")) == 0

# def test_get_all():
#     response = client.get("/recipe")
#     assert response.status_code == 200
#     # response_json = response.json()
#     # assert response_json.get("message") == "Success retrieve all data"
#     # assert len(response_json.get("result")) == 0
