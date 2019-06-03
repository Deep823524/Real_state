from django.db import models

class Home(models.Model):
    home_image = models.ImageField(upload_to='image/home')
    keyword = models.CharField(max_length=50)
    location = models.TextField()
    property_type = models.CharField(max_length=50)
    property_status = models.CharField(max_length=50)
    agent_name = models.CharField(max_length=50)
    total_bedroom = models.IntegerField()
    total_bathroom = models.IntegerField()
    minimum_price = models.DecimalField(max_digits=10,decimal_places=2)
    maximum_price = models.DecimalField(max_digits=10,decimal_places=2)
    minimum_area = models.DecimalField(max_digits=10,decimal_places=2)
    maximum_area = models.DecimalField(max_digits=10,decimal_places=2)


