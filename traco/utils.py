# accounts/utils.py
import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return str(random.randint(100000, 999999))  # 6-digit OTP

def send_otp_email(email, otp):
    subject = "Your OTP Code"
    message = f"Your OTP code is {otp}. It is valid for 5 minutes."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
