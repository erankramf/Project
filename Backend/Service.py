from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


from Database import get_telescopes_list, get_telescope_parameters

async def get_telescopes():
    telescope_list = await get_telescopes_list()
    return telescope_list

async def get_params_by_name(telescope_name: str):
    params_list = await get_telescope_parameters(telescope_name)
    return params_list
