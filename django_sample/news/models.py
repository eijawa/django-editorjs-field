from django.db import models

from django_editorjs_field import EditorJSField


class Article(models.Model):
    title = models.CharField(max_length=256)

    description = EditorJSField()

    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"