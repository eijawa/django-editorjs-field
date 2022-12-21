from django.db import models

from .tool import EditorJSTool as Tool
from .widget import EditorJSWidget


class EditorJSField(models.JSONField):
    description = "An EditorJS field."

    def __init__(self, *args, **kwargs):
        unexceptable_kwargs = ["holderId", "holder", "onReady", "onChange"]

        for u_k in unexceptable_kwargs:
            if u_k in kwargs.keys():
                del kwargs[u_k]

        self.config = kwargs.copy()

        if "tools" in self.config.keys():
            self.config["tools"] = list(set(self.config["tools"]))

        kwargs.clear()
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        # Удаление созданных в конструкторе полей

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs["widget"] = EditorJSWidget(config=self.config)
        return super().formfield(**kwargs)
