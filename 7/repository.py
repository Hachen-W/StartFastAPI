from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.tasks import TasksModel
from schemas.task import STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(
        cls, data: STaskAdd,
        session: AsyncSession
    ) -> TasksModel:
        task_dict = data.model_dump()
        task = TasksModel(**task_dict)
        session.add(task)
        await session.commit()
        await session.refresh(task)

        return task

    @classmethod
    async def find_all(cls, session: AsyncSession):
        query = select(TasksModel)
        result = await session.execute(query)
        tasks_models = result.scalars().all()

        return tasks_models

    @classmethod
    async def find_one(cls, task_id: int, session: AsyncSession):
        query = select(TasksModel).where(TasksModel.id == task_id)
        result = await session.execute(query)
        task_model = result.scalars().first()

        return task_model

    @classmethod
    async def delete_one(cls, task_id: int, session: AsyncSession):
        query = delete(TasksModel).where(TasksModel.id == 5)
        await session.execute(query)
        await session.commit()
