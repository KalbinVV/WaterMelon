import json

from core.response.Response import Response


class JsonResponse(Response):
    def __init__(self, content, status=200, content_type='text/json'):
        super().__init__(json.dumps(content), status, content_type)
