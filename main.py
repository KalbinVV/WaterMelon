import json

from core.WaterMelonServer import WaterMelonServer
from core.response.HtmlResponse import HtmlResponse
from path.PathsHandler import register_path


@register_path('/')
def index_page(request):
    user = request.user

    if user.contains_data('name'):
        return HtmlResponse(f"Hello, {user.get_data('name')}")
    else:
        return HtmlResponse("I don't know your name")


@register_path('forum/<article:str>', 'GET')
def forum(request, article):
    return HtmlResponse(f'<h1>Forum!</h1><p>{article}</p>')


@register_path('api/set_name/', 'POST')
def set_user_name(request):
    user = request.user

    if 'name' not in request.post_dictionary:
        return HtmlResponse(json.dumps({'status': False, 'reason': 'Invalid args!'}))

    user.set_data('name', request.post_dictionary['name'])

    return HtmlResponse(json.dumps({'status': True}))


def main():
    server = WaterMelonServer()
    server.run()


if __name__ == '__main__':
    main()
