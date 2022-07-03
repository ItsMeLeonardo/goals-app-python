import os
from fastapi import FastAPI
from src.posts.graphic_data_service.by_tags.service import (router as by_tag_router)

import uvicorn

app = FastAPI()
app.include_router(by_tag_router)


@app.get("/")
async def root():
  return {"message": "Welcome to fastAPI"}


if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=8000)), log_level="info")
