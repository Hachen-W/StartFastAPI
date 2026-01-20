import uvicorn
from fastapi import FastAPI, status, HTTPException
from schemas import STaskAdd, STask

app = FastAPI()
tasks = [{"id": 1, "name": "Тест"}, {"id": 2, "name": "Код"}]


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd) -> STask:
    task_dict = task.model_dump()
    task_id = len(tasks) + 1
    task_dict["id"] = task_id
    tasks.append(task_dict)

    return task_dict


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Задача с ID {task_id} не найдена"
    )


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
