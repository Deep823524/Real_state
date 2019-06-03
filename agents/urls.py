# djangotemplates/agents/urls.py

from django.conf.urls import url
from agents import views

urlpatterns = [
    url(r'^agents/$', views.AgentsPageView.as_view(), name='agents'), # Notice the URL has been named

]