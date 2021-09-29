from django.urls import path

from .views import UserProfileRegister, login_page, logout_user

urlpatterns = [
    path('register',UserProfileRegister.as_view(),name="user_register"),
    path('login/',login_page,name='login'),
    path('logout', logout_user,name="logout")
]