from dotenv import dotenv_values
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env
env_vars = dotenv_values(".env")

# Get the MongoDB URL
mongodb_uri = env_vars.get("MONGODB_URI")
if not mongodb_uri:
    raise EnvironmentError("MongoDB URI not found in .env file")

client = AsyncIOMotorClient(mongodb_uri)
db = client.blog_db
