from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from django.urls import reverse_lazy

# Create your views here.
class UserProfileRegister(CreateView):
    model=User
    fields=['username','email','last_name','name','profile_picture','phone_number','short_description','password']
    

    
    def get_success_url(self):
        
        return reverse_lazy('home')+'?ok'


  