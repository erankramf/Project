
#Just copied from example Github, changed the url. Not sure if works. 
#Anyone can change when doing the connect to db ticket
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://read:XgFXpjCQZznKddf4KvtW@cta-simpipe-protodb.zeuthen.desy.de/?authMechanism=DEFAULT&authSource=admin&tls=true')

#database = client.TodoList
#collection = database.todo


import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
# Replace the placeholder with your Atlas connection string
uri = "mongodb://read:XgFXpjCQZznKddf4KvtW@cta-simpipe-protodb.zeuthen.desy.de/?authMechanism=DEFAULT&authSource=admin&tls=true"
# Set the Stable API version when creating a new client
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client["CTA-Simulation-Model"]
telescopes_collection = db["telescopes"]
async def ping_server():
  # Send a ping to confirm a successful connection
  try:
    await client["CTA-Simulation-Model"].command('ping')  
    print("Pinged your deployment. You successfully connected to MongoDB!")
    return "Pinged your deployment. You successfully connected to MongoDB!"
  except Exception as e:
    print(e)
    return str(e)
      

async def print_client():
    return await ping_server()
