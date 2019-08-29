from model.base import BaseModel

class Channel(BaseModel):
    def __init__(self, name, user_id) -> None:
        self.user_id = user_id
        self.name = name
        super().__init__()
