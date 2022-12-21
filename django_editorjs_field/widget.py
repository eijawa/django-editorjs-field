import json

from django.forms import Widget, Media
from django.utils.safestring import mark_safe
from django.forms.renderers import get_default_renderer


class EditorJSWidget(Widget):
    template_name = "widget.html"

    def __init__(self, *args, **kwargs):
        self.config = kwargs.pop("config", {})
        super().__init__(*args, **kwargs)

    @property
    def media(self):
        js = [
            "//cdn.jsdelivr.net/npm/@editorjs/editorjs",
            "//cdn.jsdelivr.net/npm/@editorjs/header",
            "django_editorjs_field/js/editor.js",
        ]

        return Media(js=js, css={"all": [""]})

    def render(self, name, value, attrs=None, renderer=None):
        if not renderer:
            renderer = get_default_renderer()

        context = self.get_context(name, value, attrs)
        context["widget"].update(
            {
                "config": json.dumps(self.config),
            }
        )

        return mark_safe(
            renderer.render(
                "django_editorjs_field/widget.html",
                context,
            )
        )
