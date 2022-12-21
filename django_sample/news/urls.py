from django.urls import path

from .views import ArticlesListView


urlpattern = [
    path("", ArticlesListView.as_view(), "articles_list")
]