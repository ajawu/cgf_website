from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False, max_length=500)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class JoinRequest(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"