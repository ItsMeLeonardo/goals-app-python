import os
from fastapi import FastAPI
from decouple import config

import uvicorn

from src.database import (get_posts)

app = FastAPI()

@app.get("/")
async def root():
  post = await get_posts()
  # print(post + '--get--')
  return {"status": "200", "data": post}


@app.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}


if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=8000)), log_level="info")
