# djangotemplates/signup/urls.py

from django.conf.urls import url
from singnup import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^singnup/$', views.SingnupPageView.as_view(), name='singnup'), # Notice the URL has been named
    url(r'^registerBox/$', views.RegisterView, name='registerBox'),
    url(r'^login/$', views.LoginPageView.as_view(), name='login'), # Notice the URL has been named
]