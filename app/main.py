from fastapi import FastAPI
from app.api.v1.api import api_router
import uvicorn
from dotenv import load_dotenv
from app.db.create_tables import create_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

load_dotenv()


app.include_router(router=api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
