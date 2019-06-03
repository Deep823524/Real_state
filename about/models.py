from django.db import models


class About(models.Model):
    about_us = models.TextField()
    about_image = models.ImageField(upload_to="image/about")
    video = models.FileField(upload_to="video/about")
