from fastapi import FastAPI

from src.routers.recipe import router as recipe_router


app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

app.include_router(recipe_router)
