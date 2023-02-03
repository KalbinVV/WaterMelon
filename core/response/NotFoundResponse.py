from core.response.HtmlResponse import HtmlResponse


class NotFoundResponse(HtmlResponse):
    def __init__(self, content):
        super().__init__(content=content, status=404)
