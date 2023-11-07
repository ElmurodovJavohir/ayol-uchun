from django.db import models
from django.contrib.auth import get_user_model
from blog.models import BlogImages


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(BlogImages, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        
    def __str__(self):
        return self.title
