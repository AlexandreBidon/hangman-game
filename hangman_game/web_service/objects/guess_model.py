from pydantic import BaseModel


class Guess(BaseModel):
    letter: str

    def __init__(self, mot, erreurs, letter):
        self.letter = letter
