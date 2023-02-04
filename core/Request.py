class Request:
    def __init__(self, url, address, method, user, get_dictionary=None, post_dictionary=None):
        if post_dictionary is None:
            post_dictionary = {}

        if get_dictionary is None:
            get_dictionary = {}

        self.url = url
        self.address = address
        self.method = method
        self.user = user
        self.get_dictionary = get_dictionary
        self.post_dictionary = post_dictionary
