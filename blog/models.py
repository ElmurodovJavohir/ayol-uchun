from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class BlogCategory(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="blog_images")

    def __str__(self) -> str:
        return str(self.id)


class Comment(models.Model):
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
