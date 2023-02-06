from core.Middleware import middleware
from core.Template import Template
from core.WaterMelonServer import WaterMelonServer
from core.response.HtmlResponse import HtmlResponse
from core.response.JsonResponse import JsonResponse
from core.response.TemplateResponse import TemplateResponse
from path.PathsHandler import register_path


def role_middleware(request):
    user = request.user

    if not user.contains_data('role'):
        return HtmlResponse('<h1>You are not authorised!</h1>')


@register_path('/')
@middleware(target=role_middleware)
def index_page(request):
    user = request.user

    if user.contains_data('name'):
        return HtmlResponse(f"Hello, {user.get_data('name')}")
    else:
        return HtmlResponse(f"I don't know you, {user.get_address()}")


@register_path('forum/<article:str>', 'GET')
def forum(request, article):
    return HtmlResponse(f'<h1>Forum!</h1><p>{article}</p>')


@register_path('api/set_name/', 'POST')
def set_user_name(request):
    user = request.user

    if 'name' not in request.post_dictionary:
        return JsonResponse({'status': False, 'reason': 'invalid args!'})

    user.set_data('name', request.post_dictionary['name'])

    return JsonResponse({'status': True})


@register_path('test_template/')
def test_template(request):
    user = request.user

    name = user.get_data('name', 'default name')

    return TemplateResponse(Template('index.html', name=name))


@register_path('api/set_role/', 'POST')
def set_user_role(request):
    if 'role' not in request.post_dictionary:
        return JsonResponse({'status': False, 'reason': 'invalid args'})

    role = request.post_dictionary['role']
    user = request.user
    user.set_data('role', role)

    return JsonResponse({'status': True})


def main():
    server = WaterMelonServer()
    server.run()


if __name__ == '__main__':
    main()
