from django.db import models
from django.utils import timezone


# Create your models here.
class Daisy(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="image", blank=True,null=True)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title