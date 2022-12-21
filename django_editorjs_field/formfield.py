from django import forms

from .widget import EditorJSWidget


class EditorJSFormField(forms.Field):
    def __init__(self, *args, **kwargs):
        self.widget = EditorJSWidget(config=kwargs.pop("config", {}))
        super().__init__(*args, **kwargs)
    