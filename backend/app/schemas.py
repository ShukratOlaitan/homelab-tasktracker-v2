from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = {
        "from_attributes": True
    }
