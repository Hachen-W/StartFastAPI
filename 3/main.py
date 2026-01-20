import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import STaskAdd, STask

app = FastAPI()

tasks = []

@app.post("/tasks")
async def create_task(task: STaskAdd) -> STask:
    task_dict = task.model_dump()

    task_id = len(tasks) + 1
    task_dict["id"] = task_id

    tasks.append(task_dict)

    return task_dict

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
