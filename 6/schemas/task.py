from pydantic import BaseModel, Field, ConfigDict


class STaskBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Название задачи"
    )
    description: str | None = Field(
        max_length=100
    )
    priority: int = Field(
        default=1,
        le=5
    )
    model_config = ConfigDict(from_attributes=True)


class STaskAdd(STaskBase):
    pass


class STask(STaskBase):
    id: int
