from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test/{name}")
def read_item(name: str, age: Union[int, None] = None):
    return {"name": name, "age": age}