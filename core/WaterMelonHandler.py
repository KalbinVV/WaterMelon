from http.server import BaseHTTPRequestHandler

from core.HeadersUtils import HeadersUtils
from core.WaterMelonServer import WaterMelonConfiguration
from core.Request import Request
from path.PathsHandler import PathsHandler


class WaterMelonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        get_dictionary = HeadersUtils.parse_header_content(self)
        self.process_request(self, get_dictionary=get_dictionary)

    def do_POST(self):
        post_dictionary = HeadersUtils.parse_header_content(self)
        self.process_request(self, post_dictionary=post_dictionary)

    @staticmethod
    def process_request(request_handler: BaseHTTPRequestHandler, get_dictionary=None, post_dictionary=None) \
            -> None:
        if post_dictionary is None:
            post_dictionary = {}

        if get_dictionary is None:
            get_dictionary = {}

        address = request_handler.client_address[0]

        users_storage = WaterMelonConfiguration.users_storage
        user = users_storage.get_user(address)

        request = Request(url=request_handler.path, address=address, method=request_handler.command, user=user,
                          get_dictionary=get_dictionary, post_dictionary=post_dictionary)

        path, implemented = PathsHandler.match_url(request.url, request.method)

        if path is None:
            response = WaterMelonConfiguration.error_404_response
        else:
            if implemented:
                response = path.run_caller(request)
            else:
                response = WaterMelonConfiguration.error_501_response

        request_handler.send_response(response.status)

        request_handler.send_header("Content-type", response.content_type)
        request_handler.end_headers()

        request_handler.wfile.write(bytes(response.content, "utf-8"))
