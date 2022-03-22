from fastapi import FastAPI
from typing import Optional, Any
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    data: Optional[Any] = None


@app.post("/")
async def root(data: Data):
    print(data)
    return data
