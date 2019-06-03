# djangotemplates/agents/views.py
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking Property  all this time :)
class AgentsPageView(TemplateView):
    template_name = "agents/agents.html"


class RegisterView(ListView):
    pass