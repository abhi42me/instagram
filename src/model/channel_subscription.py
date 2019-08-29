from model.base import BaseModel

class ChannelSubscription(BaseModel):
    def __init__(self, channel_id, user_id):
        self.channel_id = channel_id
        self.user_id = user_id
        super().__init__()
