from django.db import models

from utils.models import BaseModel

# Create your models here.
class Advertisement(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        
class UsersRule(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Users Rule'
        verbose_name_plural = 'Users Rules'
