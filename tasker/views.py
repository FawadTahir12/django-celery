from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasker.tasks import send_notification_mail
from celerydjango.settings import development
from django.core.mail import send_mail

@api_view(['POST'])
def test_api(request):
    email = request.data.get('email')
    msg = request.data.get('msg')
    send_notification_mail.delay(email, msg)
    return Response({"status":"success"})

    


