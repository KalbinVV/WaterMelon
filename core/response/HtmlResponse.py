from core.response.Response import Response


class HtmlResponse(Response):
    def __init__(self, content, status=200, content_type='text/html'):
        super().__init__(content, status, content_type)
