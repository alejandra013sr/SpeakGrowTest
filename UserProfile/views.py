from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import UserRegisterForm

# Create your views here.
class UserProfileRegister(CreateView):
    form_class = UserRegisterForm
    template_name= "UserProfile/user_form.html"
    
    def get_success_url(self):
        
        return reverse_lazy('home')+'?ok'

    

    

def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    else: 
        if request.method == 'POST':
            username= request.POST.get('username')
           
            password = request.POST.get('password')
          

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                
                return redirect(reverse('home')+'?login')

            else:
                messages.warning(request, 'You are not registered, try again')

        return render (request,'UserProfile/user_login.html',{
            'title': 'Identificate'
        })

def logout_user(request):
    logout(request)

    return redirect('home')


  