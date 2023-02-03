import re

from core.Request import Request
from core.response.Response import Response


class Path:
    def __init__(self, pattern: str, caller):
        self.pattern = self.make_regex_from_pattern(pattern)
        self.caller = caller

    @classmethod
    def get_regex_group_from_field_type(cls, field_type: str) -> str | None:
        try:
            return {
                'int': r'\d+',
                'str': r'\w+'
            }[field_type]
        except KeyError:
            return None

    @classmethod
    def make_regex_from_pattern(cls, pattern: str) -> re:
        fields_pattern = re.compile(r'<(?P<field_name>\w+):(?P<type>\w+)>')

        matches = fields_pattern.findall(pattern)

        if matches is None:
            return None

        final_pattern = f"^/?{pattern[0: pattern.find('/<')]}"

        for match in matches:
            field_name = match[0]
            field_type = match[1]

            regex_type_group = cls.get_regex_group_from_field_type(field_type)

            final_pattern += f'/(?P<{field_name}>{regex_type_group})'

        return re.compile(f'{final_pattern}/?$')

    def is_url_match(self, url: str) -> bool:
        return self.pattern.match(url) is not None

    def parse_fields_from_url(self, url: str) -> dict:
        matches = self.pattern.match(url)

        fields = dict()

        for field_name in matches.groupdict():
            fields[field_name] = matches.group(field_name)

        return fields

    def run_caller(self, request: Request) -> Response:
        fields = self.parse_fields_from_url(request.url)

        return self.caller(request, **fields)
