class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Storage(object):
    def __init__(self) -> None:
        super().__init__()

    def save(self, object_data):
        raise NotImplemented("Not implemented")


class InMemoryStore(Storage):
    def __init__(self) -> None:
        super().__init__()


class ChannelStore(InMemoryStore, metaclass=Singleton):
    def __init__(self) -> None:
        self.current_channels = dict()
        self.user_channels = dict()
        super().__init__()

    def save(self, object_data, metaclass=Singleton):
        self.current_channels[object_data.id] = object_data
        user_id = object_data.user_id
        if user_id not in self.user_channels:
            self.user_channels[user_id] = []
        self.user_channels[user_id].append(object_data)


class UserStore(InMemoryStore, metaclass=Singleton):
    def __init__(self) -> None:
        self.users = dict()
        super().__init__()

    def save(self, object_data):
        self.users[object_data.id] = object_data


class ChannelSubscriptionStore(InMemoryStore, metaclass=Singleton):
    def __init__(self) -> None:
        self.user_subscriptions = dict()
        self.channel_users = dict()

        super().__init__()

    def save(self, object_data):
        user_id = object_data.user_id
        channel_id = object_data.channel_id
        if user_id not in self.user_subscriptions:
            self.user_subscriptions[user_id] = []

        self.user_subscriptions[user_id].append(channel_id)
        if channel_id not in self.channel_users:
            self.channel_users[channel_id] = []
        self.channel_users[channel_id].append(user_id)

    def get_user_subscriptions(self, user_id):
        return self.user_subscriptions.get(user_id, [])


class ImageStore(InMemoryStore, metaclass=Singleton):
    def __init__(self) -> None:
        self.images = dict()
        self.channel_images = dict()
        super().__init__()

    def save(self, object_data):
        image_id = object_data.id
        channel_id = object_data.channel_id

        self.images[image_id] = object_data

        if channel_id not in self.channel_images:
            self.channel_images[channel_id] = []
        self.channel_images[channel_id].append(object_data)

    def get_top_images(self, channel_id, k: int = 10):
        channel_images = self.channel_images.get(channel_id, [])
        if len(channel_images) <= k:
            return list(channel_images)
        else:
            return channel_images[-1:-k - 1]
