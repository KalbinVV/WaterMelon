from typing import Any


class User:
    def __init__(self, address: str, data=None):
        if data is None:
            data = {}

        self.address = address
        self.data = data

    def get_data(self, key: str) -> Any:
        return self.data[key]

    def contains_data(self, key: str) -> bool:
        return key in self.data

    def set_data(self, key: str, value: Any) -> None:
        self.data[key] = value
