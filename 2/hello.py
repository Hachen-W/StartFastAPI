import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def hello_name(name: str):
    return "Hello, " + name + "!"

if __name__ == "__main__":
    uvicorn.run("hello:app", host="127.0.0.1", port=8000, reload=True)
