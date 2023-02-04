from storage.User import User
from storage.UsersStorage import UsersStorage


class VirtualUsersStorage(UsersStorage):
    def __init__(self):
        self.__users = dict()

    def get_user(self, address):
        if address in self.__users:
            return self.__users[address]

        user = User(address)

        self.__users[address] = user

        return user
