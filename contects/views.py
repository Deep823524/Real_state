# djangotemplates/contects/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking Property  all this time :)
class ContectsPageView(TemplateView):
    template_name = "contects/contects.html"