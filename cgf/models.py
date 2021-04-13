from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False, max_length=500)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact #{self.id}"


class JoinRequest(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    email_address = models.EmailField(blank=False)

    def __str__(self):
        return f"#{self.id} - {self.email_address}"


class Event(models.Model):
    CHARITY = 'charity'
    EVENT_TAG_OPTIONS = [
        ('charity', 'Charity'),
        ('conference', 'Conference'),
        ('self-development', 'Self Development'),
    ]

    tag = models.CharField(max_length=20, choices=EVENT_TAG_OPTIONS, default=CHARITY)
    name = models.CharField(max_length=60, blank=False)
    location = models.CharField(max_length=100, blank=False)
    time = models.DateTimeField()
    is_holding = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)


class EventSeat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_attending = models.TextField()

    def __str__(self):
        return self.user.username
