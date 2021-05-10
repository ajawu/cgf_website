from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, blank=False)
    is_paid = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.username
