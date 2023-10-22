import os
from dataclasses import dataclass


@dataclass
class Settings:
    mongo_db_username: str = os.getenv("HAVAESH_MONGO_USERNAME")
    mongo_db_password: str = os.getenv("HAVAESH_MONGO_PASSWORD")
    mongo_db_host: str = os.getenv("HAVAESH_MONGO_HOST")
    mongo_db_name: str = os.getenv("HAVAESH_MONGO_DB_NAME")
    recipe_collection: str = os.getenv("HAVAESH_MONGO_RECIPE_COLLECTION")


settings = Settings()
