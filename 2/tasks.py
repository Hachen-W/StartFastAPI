import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_tasks_db = [
    {"task_id": 1, "task_name": "Изучить Python"},
    {"task_id": 2, "task_name": "Подключить Базу Данных"},
    {"task_id": 3, "task_name": "Выучить FastAPI"},
]

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in fake_tasks_db:
        if task["task_id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    uvicorn.run("tasks:app", host="127.0.0.1", port=8000, reload=True)
