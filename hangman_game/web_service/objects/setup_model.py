from pydantic import BaseModel


class Setup(BaseModel):
    max_error: int
