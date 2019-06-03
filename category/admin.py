from django.contrib import admin
from .models import Catagory




class AdminCetagory(admin.ModelAdmin):
    list_display = ['Catagory_id','Catagory_name','Is_Valid']

admin.site.register(Catagory,AdminCetagory)
