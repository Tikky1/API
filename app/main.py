from fastapi import FastAPI
from web.task import router

app = FastAPI()

app.include_router(router)