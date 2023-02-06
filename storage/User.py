from datetime import datetime
from typing import Any


class User:
    def __init__(self, address: str, data=None, data_expire_time: int = 300):
        if data is None:
            data = {}

        self.__address = address
        self.__data = data
        self.__last_data_timestamp = datetime.now()
        self.__data_expire_time = data_expire_time

    def get_data(self, key: str, default=None) -> Any:
        self.__last_data_timestamp = datetime.now()

        if key not in self.__data:
            return default

        return self.__data[key]

    def contains_data(self, key: str) -> bool:
        self.__last_data_timestamp = datetime.now()
        return key in self.__data

    def set_data(self, key: str, value: Any) -> None:
        self.__last_data_timestamp = datetime.now()
        self.__data[key] = value

    def get_address(self) -> str:
        return self.__address

    def is_expire(self) -> bool:
        now = datetime.now()
        duration = now - self.__last_data_timestamp

        if duration.total_seconds() >= self.__data_expire_time:
            return True
        else:
            return False
