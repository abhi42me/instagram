from data_layer.base_dao import BaseDao
from data_layer.storage_layer import ChannelStore, UserStore, ChannelSubscriptionStore, ImageStore
from util.singleton import Singleton

class ChannelDao(BaseDao, metaclass=Singleton):
    def __init__(self) -> None:
        self.channel_store = ChannelStore()
        super().__init__(self.channel_store)

    def add_image(self, image_data):
        self.channel_store.add_image(image_data)

    def get_top_channel_images(self, channel_id, k: int = 10):
        return self.channel_store.get_top_images(channel_id, k)


class ImageDao(BaseDao, metaclass=Singleton):
    def __init__(self) -> None:
        self.image_store = ImageStore()
        self.channel_dao = ChannelDao()
        super().__init__(self.image_store)

    def save(self, object_data):
        super().save(object_data)
        self.channel_dao.add_image(object_data)



class UserDao(BaseDao, metaclass=Singleton):
    def __init__(self) -> None:
        self.user_store = UserStore()
        super().__init__(self.user_store)


class ChannelSubscriptionDao(BaseDao, metaclass=Singleton):
    def __init__(self) -> None:
        self.channel_subscription_store = ChannelSubscriptionStore()
        super().__init__(self.channel_subscription_store)

    def get_user_subscriptions(self, user_id):
        return self.channel_subscription_store.get_user_subscriptions(user_id)



user_dao = UserDao()
image_dao = ImageDao()
channel_dao = ChannelDao()
channel_subscription_dao = ChannelSubscriptionDao()