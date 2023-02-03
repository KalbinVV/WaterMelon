from core.response.NotFoundResponse import NotFoundResponse


class WaterMelonConfiguration:
    server_name = 'localhost'
    server_port = 8080
    error_404_response = NotFoundResponse('<hr><h1 style="text-align: center">Error: 404</h1><hr>')
