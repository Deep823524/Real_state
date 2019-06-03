# djangotemplates/Property/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking Property  all this time :)
class PropertyPageView(TemplateView):
    template_name = "property/property.html"


class PropertysinglePageView(TemplateView):
	template_name = "property/property-single.html"
		