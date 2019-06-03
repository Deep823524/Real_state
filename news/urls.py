# djangotemplates/example/urls.py

from django.conf.urls import url
from news import views

urlpatterns = [
   # url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^news/$', views.NewsPageView.as_view(), name='news'),
]