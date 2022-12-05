from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256)

    description = models.TextField()

    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"