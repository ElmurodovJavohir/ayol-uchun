from rest_framework import serializers
from .models import *
from hitcount.models import HitCount


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = [
            "title",
            "body",
            "date",
            "author",
            "slug",
            "comments",
            "category",
        ]
