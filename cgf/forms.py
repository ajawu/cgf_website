from django import forms
from .models import Contact, JoinRequest
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['is_completed']
    
    def send_email(self):
        send_mail('New Contact Message - Classic Gentlemen', 
            f"""
Hey Admin,

{self.cleaned_data['message']}.

Thanks, {self.cleaned_data['first_name']} {self.cleaned_data['last_name']}
            """,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_CONTACT_EMAIL, self.cleaned_data['email']])


class JoinForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = '__all__'
        exclude = ['is_approved']

    def send_email(self):
        send_mail('New Join Request - Classic Gentlemen', 
            f"""Hey Admin,

My name is {self.cleaned_data['full_name']} and I am interested in joining the Classic gentlemen's social club. 
You can contact me for any additional information via phone - {self.cleaned_data['phone_number']}
or my email - {self.cleaned_data['email']}.

Thanks, {self.cleaned_data['full_name']}
            """,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_CONTACT_EMAIL])
