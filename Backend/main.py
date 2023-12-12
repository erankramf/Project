from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from Database import print_client

from Service import(
    getParamsByName,
    getTelescopeByName,
)

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/PingDatabase")
async def getter():
    response = await print_client()
    return response

#do we want all the parameters?
@app.get("getData/Telescopes/TelescopeName") #we can change how this path looks depending on the things we will need to get done
async def getParamsByName(TelescopeName):
    response = await getParamsByName(TelescopeName) #Service-Call
    if response:
        return response
    raise HTTPException(404, f"couldn't find Telescope Parameters")

#what does getting the telescope do? ByName because maybe we will also want to get them by ID
@app.get("/getData/Telescopes/{TelescopeName}")
async def getTelescopeByName(TelescopeName):
    response = await getTelescopeByName(TelescopeName)
    if response:
        return response
    raise HTTPException(404, f"couldn't find Telescope")

#maybe a "getTelescopes" function for displaying all the Telescopes that are in the Database at the moment
#I don't understand the getTelescope() one, what do we get there?


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)