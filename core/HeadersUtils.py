import re
from http.server import BaseHTTPRequestHandler


class HeadersUtils:
    @staticmethod
    def parse_header_content(request_handler: BaseHTTPRequestHandler) -> dict:
        content_length = int(request_handler.headers.get('content-length', 0))

        content = request_handler.rfile.read(content_length).decode('utf-8')

        header_content_pattern = re.compile(r'^Content-Disposition:\s*(?P<content_type>[\w+\-]+);'
                                            r'\s*name=\"(?P<content_name>\w+)\"$', re.MULTILINE)
        header_content_match = None

        values = dict()

        for line in content.split('\n'):
            trimmed_line = line.strip()

            if len(trimmed_line) == 0:
                continue

            if header_content_match is not None:
                values[header_content_match.group('content_name')] = trimmed_line

            header_content_match = header_content_pattern.match(trimmed_line)

        return values
