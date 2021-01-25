from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.dummy_user_view, name='dummy_user_view'),
]
