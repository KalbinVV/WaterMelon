from functools import wraps
from functools import lru_cache

from path.Path import Path


class PathsHandler:
    paths: Path = []

    @classmethod
    def register_path(cls, pattern, caller):
        cls.paths.append(Path(pattern, caller))

    @classmethod
    @lru_cache
    def match_url(cls, url: str) -> Path | None:
        for p in cls.paths:
            if p.is_url_match(url):
                return p

        return None


def register_path(pattern):
    def wrapped_decorator():
        def decorator(caller):
            PathsHandler.register_path(pattern, caller)
            print(f'Path registered: {pattern}')

        return decorator

    return wrapped_decorator()
