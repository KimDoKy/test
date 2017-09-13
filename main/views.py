from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.

class IndexMain(TemplateView):
    template_name = 'index.html'

class TestView(TemplateView):
    template_name = 'test.html'
