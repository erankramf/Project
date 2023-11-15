from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/pingpong")
def getter():
    return "Ping Ping"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello")
