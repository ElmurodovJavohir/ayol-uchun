from rest_framework import serializers
from .models import *


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ("title", "slug")


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True)
    category = BlogCategorySerializer()

    class Meta:
        model = Article
        fields = [
            "created_at",
            "updated_at",
            "title",
            "body",
            "author",
            "slug",
            "comments",
            "category",
            # "hit_count",
        ]
