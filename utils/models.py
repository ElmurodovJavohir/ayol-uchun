from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        try:
            return self.title
        except:
            return str(self.id)
=======
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
>>>>>>> 6d464fc (fix: user migrations)
