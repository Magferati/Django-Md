from django.db import models

# Create your models here.
class Daisy(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    discribtion = models.TextField(blank=True,null=True)
    

    def __str__(self):
        return self.title