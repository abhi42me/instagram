from util.id_generator import get_unique_id

class BaseDao():

    def __init__(self, storage_layer) -> None:
        self.storage_layer = storage_layer

    def save(self, data):
        data.id = get_unique_id()
        self.storage_layer.save(data)