from fastapi import APIRouter, HTTPException, status

from schemas.task import STask, STaskAdd
from database import SessionDep
from repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task(
    task: STaskAdd,
    session: SessionDep
) -> STask:
    task_model = await TaskRepository.add_one(task, session)
    return task_model


@router.get("/{task_id}")
async def get_task(
    task_id: int,
    session: SessionDep
):
    task = await TaskRepository.find_one(task_id, session)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с ID {task_id} не найдена"
        )
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    session: SessionDep
):
    await TaskRepository.delete_one(task_id, session)
    return


@router.get("")
async def get_tasks(
    session: SessionDep
):
    tasks = await TaskRepository.find_all(session)
    return tasks
