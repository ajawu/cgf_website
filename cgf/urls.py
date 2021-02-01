from django.urls import path
from . import views

app_name = 'cgf'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
]
