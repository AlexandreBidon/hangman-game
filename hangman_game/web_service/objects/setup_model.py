from pydantic import BaseModel


class Setup(BaseModel):
    max_error: int

    def __init__(self, max_error):
        self.max_error = max_error
