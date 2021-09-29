from django.urls import path

from .views import UserProfileRegister

urlpatterns = [
    path('register',UserProfileRegister.as_view(),name="user_register")
    
]