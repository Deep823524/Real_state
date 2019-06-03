# djangotemplates/Perproty/urls.py

from django.conf.urls import url
from property import views

urlpatterns = [
    url(r'^property/$', views.PropertyPageView.as_view(), name='property'), # Notice the URL has been named
    url(r'^property-sinle/$', views.PropertysinglePageView.as_view(), name='property-sinle'), # Notice the URL has been named
]