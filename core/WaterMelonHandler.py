from http.server import BaseHTTPRequestHandler

from core.WaterMelonServer import WaterMelonConfiguration
from core.Request import Request
from path.PathsHandler import PathsHandler


class WaterMelonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        address = self.client_address[0]

        users_storage = WaterMelonConfiguration.users_storage
        user = users_storage.get_user(address)

        request = Request(url=self.path, address=address, method=self.command, user=user)

        path = PathsHandler.match_url(request.url)

        if path is None:
            response = WaterMelonConfiguration.error_404_response
        else:
            response = path.run_caller(request)

        self.send_response(response.status)

        self.send_header("Content-type", response.content_type)
        self.end_headers()

        self.wfile.write(bytes(response.content, "utf-8"))
