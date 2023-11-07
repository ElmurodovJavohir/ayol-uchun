from rest_framework import serializers
from .models import *
from hitcount.models import HitCount


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ("title", "slug")


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class HitCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitCount
        fields = ["hits"]


class ArticleSerializer(serializers.ModelSerializer):
    hit_count = HitCountSerializer(source="hit_count_generic")
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
            "hit_count",
        ]
