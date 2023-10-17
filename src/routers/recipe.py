from fastapi import APIRouter
from src.services.recipe import RecipeService
from src.models.recipe import Recipe
from src.schemas.recipe import Response

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
)


@router.get("/")
async def get_all():
    _recipeList = await RecipeService.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=_recipeList)


@router.post("/create")
async def create(recipe: Recipe):
    await RecipeService.insert(recipe)
    return Response(code=200, status="Ok", message="Success save data")


@router.get("/{id}")
async def get_id(id: str):
    _recipe = await RecipeService.retrieve_id(id)
    return Response(code=200, status="Ok", message="Success retrieve data", result=_recipe)


@router.post("/update")
async def update(recipe: Recipe):
    await RecipeService.update(recipe.id, recipe)
    return Response(code=200, status="Ok", message="Success update data")


@router.delete("/{id}")
async def delete(id: str):
    await RecipeService.delete(id)
    return Response(code=200, status="Ok", message="Success delete data")
