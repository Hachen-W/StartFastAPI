from fastapi import APIRouter, HTTPException, status
from schemas.task import STask, STaskAdd

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)
status.HTTP_404_NOT_FOUND
tasks = [{"id": 1, "name": "Тест"}, {"id": 2, "name": "Код"}]


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd) -> STask:
    task_dict = task.model_dump()
    task_id = len(tasks) + 1
    task_dict["id"] = task_id
    tasks.append(task_dict)

    return task_dict


@router.get("/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Задача с ID {task_id} не найдена"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )


@router.get("")
async def get_tasks():
    return tasks
