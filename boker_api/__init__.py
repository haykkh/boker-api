import os
import asyncio
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from boker_api.routers import topup, balances
from boker_api.bot import client

load_dotenv()

app = FastAPI()

origins = [
    'https://localhost',
    'https://boker.hayk.earth',
    'https://boker.haykkh.vercel.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(client.start(os.getenv('DISCORD_BOT_TOKEN')))


@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(
    topup.router,
    prefix="/topup",
    tags=["topup"]
)
app.include_router(
    balances.router,
    prefix="/balances",
    tags=["balances"]
)
