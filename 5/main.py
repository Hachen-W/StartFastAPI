import uvicorn
from fastapi import FastAPI
from routers.task import router as tasks_router


app = FastAPI()
app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
