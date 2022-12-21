from django.db import models


class EditorJSField(models.JSONField):
    description = "An EditorJS field."

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        # Удаление созданных в конструкторе полей

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # Функция для получения Widget этого поля в форме
        return super().formfield(**kwargs)

    def render(self):
        # Функция для преобразования JSON-данных в HTML
        pass