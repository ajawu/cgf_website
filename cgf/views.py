from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect
from django.http import Http404
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'cgf/index.html'


class AboutView(TemplateView):
    template_name = 'cgf/about.html'


class ContactView(CreateView):
    template_name = 'cgf/contact.html'
    form_class = ContactForm
