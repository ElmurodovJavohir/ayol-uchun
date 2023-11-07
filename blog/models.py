from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation


class BlogCategory(models.Model):
    title = models.CharField(max_length=128)

    slug = models.SlugField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    body = RichTextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(unique=True, editable=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            num = 1
            while Article.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{num}"
                num += 1

        super().save(*args, **kwargs)


class BlogImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="blog_images")

    def __str__(self) -> str:
        return str(self.id)


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )

    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
