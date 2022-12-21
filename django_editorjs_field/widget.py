from django.forms import Widget
from django.template import loader
from django.utils.safestring import mark_safe
from django.forms.renderers import get_default_renderer

import os
PACKAGE_DIR = os.path.dirname(__file__)
print(PACKAGE_DIR)

class EditorJSWidget(Widget):
    template_name = "widget.html"

    def __init__(self, *args, **kwargs):
        print("You called a widget")
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        renderer = get_default_renderer()
        template = renderer.render("django_editorjs_field/widget.html", self.get_context(name, value, attrs))
        return mark_safe(template)