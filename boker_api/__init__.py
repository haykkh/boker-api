from fastapi import FastAPI

from boker_api.routers import topup, balances

app = FastAPI()


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
