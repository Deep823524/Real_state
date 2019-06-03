from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    contact_us = models.BigIntegerField()
    comment_us = models.TextField()

