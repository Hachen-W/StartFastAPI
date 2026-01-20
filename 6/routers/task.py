from fastapi import APIRouter, HTTPException, status

from sqlalchemy import select, delete

from schemas.task import STask, STaskAdd
from models.tasks import TasksModel
from database import SessionDep


router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task(
    task: STaskAdd,
    session: SessionDep
) -> STask:
    new_task = TasksModel(**task.model_dump())
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


@router.get("/{task_id}")
async def get_task(
    task_id: int,
    session: SessionDep
):
    query = select(TasksModel).where(TasksModel.id == task_id)
    result = await session.execute(query)
    task = result.scalars().first()

    if task is not None:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Задача с ID {task_id} не найдена"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    session: SessionDep
):
    query = delete(TasksModel).where(TasksModel.id == 5)

    await session.execute(query)
    await session.commit()

    return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )


@router.get("")
async def get_tasks(
    session: SessionDep
):
    query = select(TasksModel)
    result = await session.execute(query)
    return result.scalars().all()
