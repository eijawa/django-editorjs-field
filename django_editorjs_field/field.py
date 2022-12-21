from django.db import models

from .formfield import EditorJSFormField


class EditorJSField(models.Field):
    description = "An EditorJS field."

    def __init__(self, *args, **kwargs) -> None:
        self.config = kwargs.pop("config", {})
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        # Удаление созданных в конструкторе полей

        return name, path, args, kwargs

    def formfield(self, **kwargs):
        return super().formfield(**{
            "form_class": EditorJSFormField,
            "config": self.config,
            **kwargs
        })

    def get_internal_type(self) -> str:
        return "EditorJSField"

    # def render(self):
    #     # Функция для преобразования JSON-данных в HTML
    #     pass