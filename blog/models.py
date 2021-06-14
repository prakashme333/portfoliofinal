from django.db import models

# Create your models here.
class blog (models.Model):
   title = models.CharField(max_length=200)
   date = models.DateTimeField()
   description = models.TextField()

   def __str__(self):
       return self.title
   