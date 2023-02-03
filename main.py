from core.response.HtmlResponse import HtmlResponse
from core.WaterMelonServer import WaterMelonServer
from path.PathsHandler import register_path


@register_path('')
def index(request):
    return HtmlResponse('<h1>Hello, world!</h1>')


@register_path('/user/<name:str>')
def user_page(request, name):
    return HtmlResponse(f'<h4>Hello, {name}!<h4>')


@register_path('forum/page/<userid:int>/<article_name:str>')
def forum(request, userid, article_name):
    return HtmlResponse(f'<h1>{article_name}</h1><p>id: {userid}</p>')


def main():
    server = WaterMelonServer()
    server.run()


if __name__ == '__main__':
    main()
