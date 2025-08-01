from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=300)
    phone = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' + self.name 