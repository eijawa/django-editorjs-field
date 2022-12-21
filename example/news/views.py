from django.views.generic import ListView

from .models import Article

from django_editorjs_field.utils import render

class ArticlesListView(ListView):
    model = Article
    template_name = "articles-list.html"
    context_object_name = "articles_list"