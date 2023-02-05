import threading
from http.server import HTTPServer

from core.WaterMelonConfiguration import WaterMelonConfiguration
from core.WaterMelonHandler import WaterMelonHandler


class WaterMelonServer(HTTPServer):
    def __init__(self):
        server_name = WaterMelonConfiguration.server_name
        server_port = WaterMelonConfiguration.server_port

        super().__init__((server_name, server_port), WaterMelonHandler)

    def run(self):
        print(f'Server started: {self.server_name}:{self.server_port}')

        users_storage = WaterMelonConfiguration.users_storage

        data_cleaner_thread = threading.Thread(target=users_storage.data_cleaner)

        data_cleaner_thread.start()

        try:
            self.serve_forever()
        except KeyboardInterrupt:
            print('Closing server...')

        self.server_close()

        if users_storage.is_data_cleaner_enabled():
            users_storage.disable_data_cleaner()
            print('Data cleaner stop working, it may spend some time...')

        data_cleaner_thread.join()

        print('Server closed!')
