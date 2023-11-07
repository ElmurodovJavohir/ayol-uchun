from django.db import models
from django.contrib.auth import get_user_model
from blog.models import BlogImages


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ForeignKey(BlogImages, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )