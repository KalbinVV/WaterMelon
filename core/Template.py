from jinja2 import Template as JinjaTemplate


class Template:
    def __init__(self, path_to_file: str, **kwargs):
        with open(path_to_file, 'r') as file:
            lines = file.readlines()

        template = JinjaTemplate('\n'.join(lines))

        self.__content = template.render(**kwargs)

    def get_content(self):
        return self.__content
