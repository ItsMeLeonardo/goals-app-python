import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_URI") # lee lq variable del environment (.env)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['test']


post_collection = database.get_collection("posts")

print(database, 'db')
print(client, 'client')
print(post_collection, 'post_collection')

# helpers student function
def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "url": post["url"],
        "title": post["title"],
        # "tags": post["tags"],
    }

# crud operations
# Recuperar todos los alumnos presentes en la base de datos
async def get_posts():
    students = []

    async for post in post_collection.find():
        print(post, 'students')
        students.append(post_helper(post))


    return students
