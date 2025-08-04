from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=150)
    heading = models.CharField(max_length=20)
    content = models.TextField()
    slug = models.CharField(max_length=100 , blank=True , null=True)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.author

