from django.shortcuts import render
from django.views.generic import TemplateView

class ConvertView(TemplateView):
    template_name = 'index.html'