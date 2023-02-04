from core.response.HtmlResponse import HtmlResponse
from core.response.NotFoundResponse import NotFoundResponse
from storage.VirtualUsersStorage import VirtualUsersStorage


class WaterMelonConfiguration:
    server_name = 'localhost'
    server_port = 8080
    error_404_response = NotFoundResponse('<hr><h1 style="text-align: center">Error: 404</h1><hr>')
    error_501_response = HtmlResponse('<hr><h1 style="text-align: center">Error: 501</h1><hr>', status=501)
    users_storage = VirtualUsersStorage(data_cleaner_enabled=True,
                                        data_cleaner_frequency_time=30,
                                        data_expire_time=15*60)
    show_paths_registering = True
    show_regexes_for_paths = False
