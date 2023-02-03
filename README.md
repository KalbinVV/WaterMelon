# WaterMelon
Simple backend framework inspired by **Flask**

Python version: **3.10**

## Example of use:

### Main function:
    def main():

        server = WaterMelonServer()

        server.run()

### Page registering:
    @register_path('forum/page/<userid:int>/<article_name:str>')
    def forum(request, userid, article_name):
        return HtmlResponse(f'<h1>{article_name}</h1><p>id: {userid}</p>')

### Storage use:
    @register_path('/')
    def index_page(request):
        user = request.user

        if user.contains_data('name'):
            return HtmlResponse(f"Hello, {user.get_data('name')}")
        else:
            return HtmlResponse("I don't know your name")


## Functionality:

1. Url patterns
2. Permanent storage for users data binded by ip 
3. Configuration file

## Todo:
1. Sessions
2. Cookies
3. Post, get processing
4. Docs