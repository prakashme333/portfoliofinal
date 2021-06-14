from django.db import models

# Create your models here.
class contact (models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=254)
   subject = models.CharField(max_length=100)
   message = models.CharField(max_length=500)

   def __str__(self):
       return self.name
   
class about_service (models.Model):
    aboutme = models.TextField()
    web_service = models.TextField()
    app_service = models.TextField()
    digitalmarketing_service = models.TextField()
    skill = models.TextField()
