from django import forms

from .widget import EditorJSWidget


class EditorJSFormField(forms.Field):
    # widget = EditorJSWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = EditorJSWidget()
    