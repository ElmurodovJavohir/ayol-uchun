from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import *
from hitcount.views import HitCountDetailView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from .serializers import *
from rest_framework import permissions


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(HitCountDetailView):
    model = Article
    count_hit = True


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "summary",
        "body",
        "photo",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = (
        "title",
        "summary",
        "body",
        "photo",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


#### API Views
class BlogCategoryAPIView(ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    def get_queryset(self):
        article_slug = self.kwargs.get("slug")

        return Article.objects.filter(slug=article_slug)


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdsDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
