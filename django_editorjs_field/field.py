from django.db import models

from .widget import EditorJSWidget


class EditorJSField(models.JSONField):
    description = "An EditorJS field."

    def __init__(self, *args, **kwargs) -> None:
        self.config = kwargs.copy()
        kwargs.clear()
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        # Удаление созданных в конструкторе полей

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        kwargs["widget"] = EditorJSWidget(config=self.config)
        return super().formfield(**kwargs)

    # def render(self):
    #     # Функция для преобразования JSON-данных в HTML
    #     pass