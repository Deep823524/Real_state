
from django.db import models
from django.utils import timezone

from category.models import Catagory

class News(models.Model):
    News_id = models.IntegerField(primary_key=True)
    Heading = models.CharField(max_length=50)
    Short_description = models.TextField()
    Full_description = models.TextField()
    Created_by = models.CharField(max_length=30)
    Created_at = models.DateTimeField(default=timezone.now)
    Modified_by = models.CharField(max_length=30)
    Modified_at = models.DateTimeField(default=timezone.now)
    Category_id = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='images/news')



