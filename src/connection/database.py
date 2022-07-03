import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_URI") # lee lq variable del environment (.env)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['test']