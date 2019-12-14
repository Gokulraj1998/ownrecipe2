from django.conf import settings
from django.shortcuts import render
from .models import Login
from .models import Newuser

from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def page1(request):
    return render(request,'home_page.html')

def signup(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['psw']
    if Login.objects.filter(email__isnull=False):
        if Login.email == email:
            return HttpResponse('email is already in use')
        else:
            obj_savelogin = Login(email = email,password = password)
             #emailing
            list = []
            list.append(email)
            subject = 'Thank you'
            from_email = settings.EMAIL_HOST_USER
            to_email   = list
            send_mail(subject,
                      'Owrecipe Account is created successfully',
                      from_email,
                      to_email,
                      fail_silently=False)
            list.clear()
            obj_savelogin.save()
            obj_newuser = Newuser(name = name, email = email, password = password, fk_login=obj_savelogin)
            obj_newuser.save()

            return HttpResponse('thank you')
    else:
        obj_savelogin = Login(email = email,password = password)
        subject = 'Thank you'
        from_email = settings.EMAIL_HOST_USER
        to_email   = ["grthambithambi@gmail.com"]
        send_mail(subject,
                      'Owrecipe Account is created successfully',
                      from_email,
                      to_email,
                      fail_silently=False)
        obj_savelogin.save()
        obj_newuser = Newuser(name = name, email = email, password = password, fk_login=obj_savelogin)
        obj_newuser.save()
        
        return HttpResponse('thank you')
    return HttpResponse('done') 