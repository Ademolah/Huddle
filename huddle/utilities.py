from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


from .models import Item

def notify_users(huddle, user):
    users = []

    for item in huddle.items.all():
        if item.user not in users:
            users.append(item.user)

    subject = f"New message in {huddle.key}"
    message = f"{user} wrote a message"
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, users)