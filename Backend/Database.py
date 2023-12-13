import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi


uri = "mongodb://read:XgFXpjCQZznKddf4KvtW@cta-simpipe-protodb.zeuthen.desy.de/?authMechanism=DEFAULT&authSource=admin&tls=true"
#uri = "mongodb://localhost:27017" #local for testing

client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
# Not quite sure these are what we need, but we can work with that and maybe change later.
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
    return repr(e)
asyncio.run(ping_server())

async def print_client():
    return await ping_server()
  
async def getParamsByName(TelName):
  cursor = telescopes_collection.find({"Telescope":TelName})
  Params = []
  async for telescope in cursor:
    if telescope not in Params:
      Params.append(telescope.get("Parameters"))
  return Params
  
  
async def getTelescopes():
  TelescopeList = []
  cursor = await telescopes_collection.find()
  async for tel in cursor:
    if tel.get("Telescope") not in TelescopeList:
      TelescopeList.append(tel.get("Telescope"))
  return TelescopeList
