
from django.db import models
from django.utils import timezone

class Catagory(models.Model):
    Catagory_id = models.IntegerField(primary_key=True)
    Catagory_name = models.CharField(max_length=30)
    Is_Valid = models.CharField(max_length=20, default='active')
    Created_at = models.DateTimeField(default=timezone.now)
    Modified_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Catagory_name