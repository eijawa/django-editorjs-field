import json

from django.forms import Widget, Media
from django.utils.safestring import mark_safe
from django.forms.renderers import get_default_renderer


class EditorJSWidget(Widget):
    template_name = "widget.html"

    def __init__(self, *args, **kwargs):
        self.config = kwargs.pop("config", {})

        super().__init__(*args, **kwargs)

        # TODO: Узнать, почему конструктор класса вызывается дважды, что ведёт к ошибке с конфигом

    @property
    def media(self):
        js = []

        for tool in self.config["tools"]:
            js.append(tool.url)

        js.extend(
            [
                "//cdn.jsdelivr.net/npm/@editorjs/editorjs",
                "django_editorjs_field/js/editor.js",
            ]
        )

        return Media(js=js, css={"all": [""]})

    def render(self, name, value, attrs=None, renderer=None):
        if not renderer:
            renderer = get_default_renderer()

        config = self.config.copy()
        if type(config["tools"]) == list:
            config["tools"] = {
                tool.__class__.__name__: tool.config for tool in config["tools"]
            }

        context = self.get_context(name, value, attrs)
        context["widget"].update(
            {
                "config": json.dumps(config),
            }
        )

        return mark_safe(
            renderer.render(
                "django_editorjs_field/widget.html",
                context,
            )
        )
