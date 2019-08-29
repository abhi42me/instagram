from model.base import BaseModel

class User(BaseModel):
    def __init__(self, name) -> None:
        self.id = None
        self.name = name
        super().__init__()
