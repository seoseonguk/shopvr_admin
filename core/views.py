from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

def send_email_to(request):
    send_mail('Subject here', 'Here is the message.', 'su.seo@bakecompany.net', ['su.seo@bakecompany.net'], fail_silently=False)
    return render(request, 'inventory/post_form.html', {
    })