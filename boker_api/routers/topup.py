import os
from fastapi import APIRouter
from pydantic import BaseModel

from boker_api.bot import client

router = APIRouter()


class TopUp(BaseModel):
    identification: str
    amount: int


@router.post("/")
async def post_topup(topup: TopUp):
    channel = client.get_channel(int(os.getenv('BOT_CHANNEL')))
    await channel.send(f'pac <@{topup.identification}> {topup.amount}')
    return f'!pac <@{topup.identification}> {topup.amount}'
