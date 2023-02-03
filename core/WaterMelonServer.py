from http.server import HTTPServer

from core.WaterMelonConfiguration import WaterMelonConfiguration
from core.WaterMelonHandler import WaterMelonHandler
from core.session.VirtualUsersStorage import VirtualUsersStorage


class WaterMelonServer(HTTPServer):
    def __init__(self):
        server_name = WaterMelonConfiguration.server_name
        server_port = WaterMelonConfiguration.server_port

        super().__init__((server_name, server_port), WaterMelonHandler)

        self.__users_storage = VirtualUsersStorage()

    def run(self):
        print(f'Server started: {self.server_name}:{self.server_port}')

        try:
            self.serve_forever()
        except KeyboardInterrupt:
            print('Closing server...')

        self.server_close()
        print('Server closed!')

    def get_users_storage(self):
        return self.__users_storage
