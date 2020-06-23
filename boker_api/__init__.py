import os
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI

from boker_api.routers import topup, balances
from boker_api.bot import client

load_dotenv()

app = FastAPI()


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
