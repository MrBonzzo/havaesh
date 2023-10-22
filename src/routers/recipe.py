from fastapi import APIRouter, Depends
from src.services.recipe import RecipeService, recipe_collection_dependency
from src.models.recipe import Recipe
from src.schemas.recipe import Response

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
)


@router.get("/")
async def get_all(db: RecipeService = Depends(recipe_collection_dependency)):
    _recipeList = await db.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=_recipeList)


@router.post("/create")
async def create(recipe: Recipe, db: RecipeService = Depends(recipe_collection_dependency)):
    recipe_id = await db.insert(recipe)
    return Response(code=200, status="nonoOk", message="Success save data", result=recipe_id)


@router.get("/{id}")
async def get_id(id: str, db: RecipeService = Depends(recipe_collection_dependency)):
    _recipe = await db.retrieve_id(id)
    return Response(code=200, status="Ok", message="Success retrieve data", result=_recipe)


@router.post("/update")
async def update(recipe: Recipe, db: RecipeService = Depends(recipe_collection_dependency)):
    await db.update(recipe.id, recipe)
    return Response(code=200, status="Ok", message="Success update data")


@router.delete("/{id}")
async def delete(id: str, db: RecipeService = Depends(recipe_collection_dependency)):
    await db.delete(id)
    return Response(code=200, status="Ok", message="Success delete data")
