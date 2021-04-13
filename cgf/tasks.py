from cgf_website.celery import app
from django.core.mail import send_mail
from django.conf import settings
from cgf_website.celery import celery_log


@app.task(bind=True)
def send_email_delayed(sender_email: str = '', message_text: str = '', sender_name: str = '', email_class: str = '',
                       recipient_email=None, sender_phone: str = ''):
    """
    Sends emails using django send_email via a celery task
    :param sender_email:
    :param message_text: Message body to be sent
    :param sender_name: Name of the sender
    :param email_class: Type of email template to use
    :param recipient_email: Email recipient list
    :param sender_phone: Email recipient list
    :return:
    """
    if email_class == 'contact':
        title = 'New Contact Message - Classic Gentlemen'
        message = f"Hey Admin, \n{message_text} \nYou can contact me via my email address {sender_email}" \
                  f"Thanks, {sender_name}"
        recipient_email = [settings.ADMIN_CONTACT_EMAIL, sender_email]
    elif email_class == 'join':
        title = "New Join Request - Classic Gentlemen"
        message = f"""Hey Admin,
My name is {sender_name} and I am interested in joining the Classic Gentlemen's Social club. 
You can contact me for any additional information via phone - {sender_phone}
or my email - {sender_email}.

Thanks, {sender_name}
            """
        recipient_email = [settings.ADMIN_CONTACT_EMAIL]
    elif email_class == 'newsletter':
        title = "Newsletter Subscription"
        message = 'Hey, \n This email was just used to subscribe to our newsletter. \nThank you for your interest in' \
                  'the Classic Gentlemen\'s Foundation.\nYou will receive an email from us once a month and your' \
                  'email address will not be shared with any other third party.\n Thanks, Debola from Classic' \
                  'Gentlemen'
    else:
        title = "Generic Email"
        message = message_text

    response = send_mail(title, message, settings.DEFAULT_FROM_EMAIL, recipient_email)
    if response == 1:
        celery_log.info('Email sent successfully')
    else:
        celery_log.error('An error occurred while sending this email')
