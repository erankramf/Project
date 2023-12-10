from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from Database import telescopes_collection

app = FastAPI()


async def get_telescope(telescope_id: str):
    # Perform logic to retrieve telescope data from the database
    telescope_data = await telescopes_collection.find_one({"_id": telescope_id})
    return telescope_data

async def add_telescope(telescope_data: dict):
    # Perform logic to add a new telescope to the database
    result = await telescopes_collection.insert_one(telescope_data)
    return result.inserted_id

