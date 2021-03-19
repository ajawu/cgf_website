from django.urls import path
from . import views

app_name = 'cgf'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('dashboard/', views.HomeView.as_view(), name='dashboard_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('contact/', views.ContactView.as_view(), name='contact_view'),
    path('join/', views.JoinRequestView.as_view(), name='join_request'),
]
