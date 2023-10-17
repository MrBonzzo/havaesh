from fastapi import FastAPI

from src.routers.recipe import router as recipe_router


app = FastAPI()

app.include_router(recipe_router)
