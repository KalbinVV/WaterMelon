from core.WaterMelonServer import WaterMelonServer
from core.response.HtmlResponse import HtmlResponse
from path.PathsHandler import register_path


@register_path('')
def index_page(request):
    user = request.user

    if user.contains_data('name'):
        return HtmlResponse(f"Hello, {user.get_data('name')}")
    else:
        return HtmlResponse("I don't know your name")


@register_path('/user/<name:str>')
def user_page(request, name):
    user = request.user

    user.set_data('name', name)

    return HtmlResponse(f'<h4>Hello, {name}!<h4>')


@register_path('forum/page/<userid:int>/<article_name:str>')
def forum(request, userid, article_name):
    return HtmlResponse(f'<h1>{article_name}</h1><p>id: {userid}</p>')


def main():
    server = WaterMelonServer()
    server.run()


if __name__ == '__main__':
    main()
