import motor.motor_asyncio

#Just copied from example Github, changed the url. Not sure if works. 
#Anyone can change when doing the connect to db ticket
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://read:XgFXpjCQZznKddf4KvtW@cta-simpipe-protodb.zeuthen.desy.de/?authMechanism=DEFAULT&authSource=admin&tls=true')
#database = client.TodoList
#collection = database.todo