from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from Database import print_client

from Service import(
    get_params_by_name,
    get_telescope_by_name,
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
@app.get("Telescopes/Names/{TelescopeName}") #we can change how this path looks
async def get_params_byName(TelescopeName):
    response = await get_params_by_name(TelescopeName) #Service-Call
    if response:
        return response
    raise HTTPException(404, f"couldn't find Telescope Parameters")

@app.get("Telescopes/Names")
async def get_telescopes():
    response = await get_telescopes()
    if response:
        return response
    raise HTTPException(404, f"couldn't find Telescope")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)