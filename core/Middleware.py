def middleware(target):

    def wrapped_decorator(caller):
        def wrapper(*args, **kwargs):
            return_value = target(*args, **kwargs)

            if return_value:
                return return_value

            return caller(*args, **kwargs)

        return wrapper

    return wrapped_decorator
