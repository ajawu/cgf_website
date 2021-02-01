from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'cgf/index.html'


class AboutView(TemplateView):
    template_name = 'cgf/about.html'
