from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.dummy_user_view, name='dummy_user_view'),
    path('login/', views.dummy_user_view, name='dummy_user_view'),
    path('register-request/', views.dummy_user_view, name='register_request'),
    path('password-set/', views.dummy_user_view, name='dummy_user_view'),
]
