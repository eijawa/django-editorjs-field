from django.db import models

from django_editorjs_field import EditorJSField
from django_editorjs_field.tool import EditorJSTool as Tool


class Article(models.Model):
    title = models.CharField(max_length=256)

    description = EditorJSField(
        tools=[
            Tool(
                name="Header",
                url="//cdn.jsdelivr.net/npm/@editorjs/header@2.7.0",
                template_name="tools/h.html",
            ),
            Tool(
                name="Code",
                url="https://cdn.jsdelivr.net/npm/@editorjs/code@2.8.0",
                class_name="CodeTool",
                template_name="tools/code.html",
            ),
        ],
        verbose_name="Body of Article",
        autofocus=False,
        # data={},
        # placeholder="EditorJSPlaceholder",
        i18n={"messages": {"toolNames": {"Heading": "Заголовок"}}},
    )

    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"
