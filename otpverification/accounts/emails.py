from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
import random

from django.core.mail import send_mail

from django.conf import settings


def send_email(email):
    subject="Your account Verification mail"
    otp=random.randint(1000,9999)
    message=f'your otp is{otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])

    user_obj=User.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save()
