from motor import motor_asyncio

from src.config import settings


MONGODB_URL = f"mongodb://{settings.mongo_db_username}:{settings.mongo_db_password}@{settings.mongo_db_host}"

client = motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.havaesh_mongo_db
