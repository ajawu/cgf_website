from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(default='Member', max_length=50)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
