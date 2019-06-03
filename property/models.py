from django.db import models


class Property(models.Model):
    property_uploaded_date = models.DateField(default=True)
    property_sale_date = models.DateField(default=True)
    property_deleted_date = models.DateField(default=True)
    property_modify_date = models.DateField(default=False)
    property_short_description = models.TextField(max_length=100)
    property_brief_description = models.TextField()
    property_uploaded_by = models.CharField(max_length=50)
    admin_name = models.CharField(max_length=50)
    property_image = models.ImageField(upload_to='image/property')
    keyword = models.CharField(max_length=50)
    property_location = models.TextField()
    property_city_address = models.CharField(max_length=50)
    property_state_address = models.CharField(max_length=50)
    property_country_address = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    property_status = models.CharField(max_length=50)
    agent_name = models.CharField(max_length=50)
    total_bedroom = models.IntegerField()
    total_bathroom = models.IntegerField()
    minimum_price = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_price = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_area = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_area = models.DecimalField(max_digits=10, decimal_places=2)

