from fastapi import FastAPI
import uvicorn

from app.api import api_router

app = FastAPI(
    title="Test task",
    description="REST API для управления пользователями",
    version="1.0.0",
)

app.include_router(api_router)

if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
