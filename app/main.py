from fastapi import FastAPI

from app.endpoints import user_access

app = FastAPI()

app.include_router(user_access.router)
