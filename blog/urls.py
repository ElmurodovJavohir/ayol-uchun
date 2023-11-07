from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
)

urlpatterns = [
    path("<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<slug:slug>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
]
