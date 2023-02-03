from core.session.User import User
from core.session.UsersStorage import UsersStorage


class VirtualUsersStorage(UsersStorage):
    def __init__(self):
        self.users = dict()

    def get_user(self, address):
        if address in self.users:
            return self.users[address]

        user = User(address)

        self.users[address] = user

        return user
