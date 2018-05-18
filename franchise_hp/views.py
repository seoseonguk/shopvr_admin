from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def franchise_hp_view(request):
    return render(request, 'franchise_hp/base.html')

from django.core.mail import send_mail

def franchise_email(request):
    if request.method =='POST':
        body = request.POST.dict()
        print(body)
        content = body['name'] +  "\n"  +"contact info : " +body["pn-middle"] +"-"+body["pn-last"]+  "\n"+ body['content']
        # if form.is_valid():
        send_mail(body['title'], content, 'su.seo@bakecompany.net', ['su.seo@bakecompany.net'], fail_silently=False)
    return render(request, 'franchise_hp/base.html')