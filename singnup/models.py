from django.db import models

class User(models.Model):
    emails = models.EmailField()
    password = models.CharField(max_length=30)
    repeatpassword = models.CharField(max_length=30)




