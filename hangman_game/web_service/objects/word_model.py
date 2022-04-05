from pydantic import BaseModel


class Word(BaseModel):
    id: int
    letters: str
