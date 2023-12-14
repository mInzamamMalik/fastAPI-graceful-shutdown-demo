from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect database here
    print("======> loading statup event");
    yield
    # Clean up connection here
    print("xxxxxxxx   shurting down event");

app = FastAPI(lifespan=lifespan)

@app.get("/")
def hello():
    return {"result": "hello world"}

@app.get("/abc")
def hello():
    return {"result": "hello world"}
    
@app.get("/xyz")
def hello():
    return {"result": "hello world"}


## to run this app
# uvicorn main:app --reload