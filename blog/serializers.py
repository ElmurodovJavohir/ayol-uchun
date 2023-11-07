from rest_framework import serializers
from .models import *
from hitcount.models import HitCount


class HitCountSerializerField(serializers.Field):
    def to_representation(self, instance):
        return (
            instance.hit_count_generic.get().hits
            if instance.hit_count_generic.exists()
            else 0
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    hit_count = HitCountSerializerField(source="*")
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
            "hit_count",
            "comments",
            "category",
        ]
