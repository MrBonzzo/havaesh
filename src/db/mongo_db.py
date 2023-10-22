from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import settings


class MongoClient:
    db_client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None
    
    @classmethod
    def init_db(cls):
        print("init")
        cls.db_client = AsyncIOMotorClient(
            settings.mongo_db_host,
            username=settings.mongo_db_username,
            password=settings.mongo_db_password,
        )
        cls.db = cls.db_client[settings.mongo_db_name]
    
    @classmethod
    def close_db(cls):
        print("close")
        
        if not cls.db_client:
            return
        cls.db_client.close()

        cls.db_client = None
        cls.db = None

    @classmethod
    def get_db(cls) -> AsyncIOMotorDatabase:
        return cls.db
