from pydantic import BaseModel


class Word(BaseModel):
    id: int
    caracteres: str

    def __init__(self, id, caracteres):
        self.id = id
        self.caracteres = caracteres
