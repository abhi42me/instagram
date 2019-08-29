from data_layer.base_dao import BaseDao
from data_layer.storage_layer import ChannelStore, UserStore, ChannelSubscriptionStore, ImageStore


class ChannelDao(BaseDao):
    def __init__(self) -> None:
        self.channel_store = ChannelStore()
        super().__init__(self.channel_store)


class ImageDao(BaseDao):
    def __init__(self) -> None:
        self.image_store = ImageStore()
        super().__init__(self.image_store)

    def get_top_channel_images(self, channel_id, k: int = 10):
        return self.image_store.get_top_images(channel_id, k)


class UserDao(BaseDao):
    def __init__(self) -> None:
        self.user_store = UserStore()
        super().__init__(self.user_store)


class ChannelSubscriptionDao(BaseDao):
    def __init__(self) -> None:
        self.channel_subscription_store = ChannelSubscriptionStore()
        super().__init__(self.channel_subscription_store)

    def get_user_subscriptions(self, user_id):
        return self.channel_subscription_store.get_user_subscriptions(user_id)



user_dao = UserDao()
image_dao = ImageDao()
channel_dao = ChannelDao()
channel_subscription_dao = ChannelSubscriptionDao()