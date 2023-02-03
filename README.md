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

#### Currently available types:
1. int **(\d+ in regex)**
2. str **(\w+ in regex)**

### Storage use:
    @register_path('/')
    def index_page(request):
        user = request.user

        if user.contains_data('name'):
            return HtmlResponse(f"Hello, {user.get_data('name')}")
        else:
            return HtmlResponse("I don't know your name")

#### Methods:
1. **contains_data(key)** - check if data with this key exists
2. **get_data(key)** - get players data
3. **set_data(key, value)** - set players data

## Functionality:

1. Url patterns
2. Permanent storage for users data binded by ip 
3. Configuration file

## Todo:
1. Sessions
2. Cookies
3. Post, get processing
4. Docs