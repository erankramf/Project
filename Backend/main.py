from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from Database import print_client

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)