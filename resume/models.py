from django.db import models


# Create your models here.
class ClientProfile(models.Model):
    name = models.CharField(max_length=255,blank=True,default='user')
    email = models.EmailField(max_length=255, blank=True,default='user@gmail.com')
    phone = models.CharField(max_length=255,blank=True,default='-')
    objective = models.TextField(max_length=1000)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    experience2 = models.CharField(max_length=255, blank=True)
    experience3 = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    github=models.URLField(max_length=255,blank=True,default='https://github.com/')
    linkedin=models.URLField(max_length=255,blank=True,default='https://www.linkedin.com/feed/')


    def __str__(self):
        return self.name
