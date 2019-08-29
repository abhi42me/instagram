from model.base import BaseModel

class Image(BaseModel):
    def __init__(self, path, user_id, channel_id) -> None:
        self.created_by_id = user_id
        self.channel_id = channel_id
        self.path = path
        super().__init__()

    def __str__(self) -> str:
        return "Path: {}, User: {}, Channel: {}".format(self.path, self.created_by_id, self.channel_id)

