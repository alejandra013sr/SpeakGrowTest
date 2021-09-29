from django.shortcuts import render
from UserProfile.models import AnonymousUser

# Create your views here.

def get_client_ip(request): 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR') 
    if x_forwarded_for: 
        ip = x_forwarded_for.split(',')[-1].strip() 
    else: 
        ip = request.META.get('REMOTE_ADDR') 
    
    return ip



def home(request): 
    ip=get_client_ip(request)

    #Verify if user already exists
    #user_anonymous = AnonymousUser.objects.filter(ip_address=ip)
    #if not(user_anonymous.exists()):
    anonymous_new= AnonymousUser()
    anonymous_new.ip_address=ip
    anonymous_new.save()


    return render(request,"home.html")