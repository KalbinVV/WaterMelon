from core.Template import Template
from core.response.HtmlResponse import HtmlResponse


class TemplateResponse(HtmlResponse):
    def __init__(self, template: Template):
        super().__init__(template.get_content())
