from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celerydjango.settings import development

logger = get_task_logger(__name__)
@shared_task
def send_notification_mail(target_mail, message):
    mail_subject = "Welcome on Board!"
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=development.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
        )
    return True

