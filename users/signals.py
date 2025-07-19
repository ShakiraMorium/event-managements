from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Welcome to EMS",
            message=f"Hi {instance.username}, welcome to our event platform!",
            from_email="admin@ems.com",
            recipient_list=[instance.email],
            fail_silently=True,
        )
