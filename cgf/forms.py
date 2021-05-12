from django import forms
from cgf.models import Contact, JoinRequest, Newsletter
from django.conf import settings
from django.core.mail import send_mail
from cgf.tasks import send_email_delayed


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['is_completed']
    
    def send_email(self):
        send_email_delayed.delay(sender_email=self.cleaned_data['email'], message_text=self.cleaned_data['message'],
                                 sender_name=f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}",
                                 email_class='contact')
        return True


class JoinForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = '__all__'
        exclude = ['is_approved']

    def send_email(self):
        send_email_delayed.delay(sender_email=self.cleaned_data['email'],
                                 sender_name=self.cleaned_data['full_name'], email_class='join', recipient_email='',
                                sender_phone=self.cleaned_data['phone_number'])
        return True


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

    def send_email(self):
        send_email_delayed(sender_email=self.cleaned_data['email_address'], email_class='newsletter')

        return True
