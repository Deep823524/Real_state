# djangotemplates/contects/urls.py

from django.conf.urls import url
from contects import views

urlpatterns = [
    url(r'^contects/$', views.ContectsPageView.as_view(), name='contects'), # Notice the URL has been named
]