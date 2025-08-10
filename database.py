from typing import Dict
from threading import Lock

class FakeDB:
    def __init__(self):
        self.items: Dict[int, dict] = {}
        self.counter = 1
        self.lock = Lock()

    def add_item(self, item_data: dict):
        with self.lock:
            item_id = self.counter
            self.items[item_id] = {**item_data, "id": item_id}
            self.counter += 1
            return self.items[item_id]

    def get_item(self, item_id: int):
        return self.items.get(item_id)

    def update_item(self, item_id: int, update_data: dict):
        with self.lock:
            if item_id in self.items:
                self.items[item_id].update(update_data)
                return self.items[item_id]
            return None

    def delete_item(self, item_id: int):
        with self.lock:
            return self.items.pop(item_id, None)

    def list_items(self, skip: int = 0, limit: int = 10):
        items_list = list(self.items.values())
        return items_list[skip:skip+limit]

db = FakeDB()
