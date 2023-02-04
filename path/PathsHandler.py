from functools import lru_cache

from core.WaterMelonConfiguration import WaterMelonConfiguration
from path.Path import Path


class PathsHandler:
    paths: list = []

    @classmethod
    def register_path(cls, pattern, caller, method):
        path = Path(pattern, caller, method)

        if WaterMelonConfiguration.show_paths_registering:
            print(f'Path registered: {pattern if len(pattern) > 0 else "/"}')

        if WaterMelonConfiguration.show_regexes_for_paths:
            print(f'Regex for {pattern if len(pattern) > 0 else "/"}: {path.pattern}')

        cls.paths.append(path)

    @classmethod
    @lru_cache
    def match_url(cls, url: str, method: str) -> Path | None:
        for p in cls.paths:
            if p.is_url_match(url):
                if p.method is None or p.method == method:
                    return p

        return None


def register_path(pattern, method=None):
    def wrapped_decorator():
        def decorator(caller):
            PathsHandler.register_path(pattern, caller, method)

        return decorator

    return wrapped_decorator()
