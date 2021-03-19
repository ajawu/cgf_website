from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect, HttpResponse
from django.http import Http404
from .forms import ContactForm, JoinForm
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'cgf/index.html'


class AboutView(TemplateView):
    template_name = 'cgf/about.html'


class ContactView(FormView):
    template_name = 'cgf/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Message saved successfully.')
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'An error occurred while saving your message')
        return super().form_invalid(form)


class JoinRequestView(FormView):
    form_class = JoinForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Message saved successfully.')
        form.save()
        return super().form_valid(form)
