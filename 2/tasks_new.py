import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_tasks_db = [
    {"task_name": "Task 1"},
    {"task_name": "Task 2"},
    {"task_name": "Task 3"},
    {"task_name": "Task 4"},
    {"task_name": "Task 5"},
    {"task_name": "Task 6"},
    {"task_name": "Task 7"},
    {"task_name": "Task 8"},
    {"task_name": "Task 9"},
    {"task_name": "Task 10"},
]

@app.get("/tasks")
async def get_tasks(limit: int = 10, offset: int = 0):
    return fake_tasks_db[offset : offset + limit]


@app.get("/tasks/filter")
async def get_tasks(limit: int = 10, offset: int = 0, keyword: str | None = None):
    answer = list()
    if keyword is not None:
        for task in fake_tasks_db:
            if keyword.lower() in task["task_name"].lower():
                answer.append(task)
    else:
        answer = fake_tasks_db.copy()
    return answer[offset : offset + limit]

if __name__ == "__main__":
    uvicorn.run("tasks_new:app", host="127.0.0.1", port=8000, reload=True)
