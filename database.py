from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client.quiz_db
results_collection = db.results

async def save_result(result):
    await results_collection.insert_one(result.dict())
