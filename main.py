from fastapi import FastAPI
from routers import chat

app = FastAPI()

app.include_router(chat.router)

@app.on_event("startup")
async def startup_event():
    await chat.gerenciador.startup_event()

@app.on_event("shutdown")
async def shutdown_event():
    await chat.gerenciador.shutdown_event()
