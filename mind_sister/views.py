from django.shortcuts import render
from django.views import generic


class HomepageView(generic.TemplateView):
    template_name = 'index.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'
