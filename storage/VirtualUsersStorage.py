from time import sleep

from storage.User import User
from storage.UsersStorage import UsersStorage


class VirtualUsersStorage(UsersStorage):
    def __init__(self, data_cleaner_enabled, data_cleaner_frequency_time, data_expire_time):
        self.__users = dict()
        self.__data_cleaner_enabled = data_cleaner_enabled
        self.__data_cleaner_frequency_time = data_cleaner_frequency_time
        self.__data_expire_time = data_expire_time

    def get_user(self, address):
        if address in self.__users:
            return self.__users[address]

        user = User(address, data_expire_time=self.__data_expire_time)

        self.__users[address] = user

        return user

    def disable_data_cleaner(self):
        self.__data_cleaner_enabled = False

    def data_cleaner(self):
        print('Data cleaner enabled!')

        while self.__data_cleaner_enabled:
            users_to_remove = []

            for user in self.__users.values():
                if user.is_expire():
                    users_to_remove.append(user)

            for user in users_to_remove:
                del self.__users[user.get_address()]

            sleep(self.__data_cleaner_frequency_time)

        print('Data cleaner stopped!')
