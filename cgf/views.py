from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView

from cgf.forms import ContactForm, JoinForm, NewsletterForm
from cgf.models import Event


class HomeView(TemplateView):
    template_name = 'cgf/index.html'


class AboutView(TemplateView):
    template_name = 'cgf/about.html'


class NewsLetterView(FormView):
    form_class = NewsletterForm
    success_url = reverse_lazy('cgf:home_view')

    def form_valid(self, form):
        form.send_email()
        form.save()
        messages.success(self.request, 'Email Address added to newsletter.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'An error occurred while saving your email address')
        return super().form_invalid(form)


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


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'cgf/dashboard.html'
    
    def get_context_data(self, **kwargs):
        return super(DashboardView, self).get_context_data(**kwargs)


class EventsList(ListView):
    model = Event
    template_name = ''
