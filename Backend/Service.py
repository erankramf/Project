from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


from Database import getTelescopesDb, getParamsByTelescopeNameDb

async def getTelescopesService():
    telescope_list = await getTelescopesDb()
    return telescope_list

async def getParamsByNameService(telescope_name: str):
    params_list = await getParamsByTelescopeNameDb(telescope_name)
    return params_list
