from django.urls import path
from cgf import views

app_name = 'cgf'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('contact/', views.ContactView.as_view(), name='contact_view'),
    path('join/', views.JoinRequestView.as_view(), name='join_request'),
    path('newsletter/', views.NewsLetterView.as_view(), name='newsletter'),
    path('events/', views.NewsLetterView.as_view(), name='events_list'),
    path('suspended/', views.SuspendedView.as_view(), name='suspended_page'),
    path('settings/personal', views.NewsLetterView.as_view(), name='settings_personal'),
]
