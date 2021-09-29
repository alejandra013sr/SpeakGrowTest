
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email= email, 
            name= name,
            last_name= last_name,
            is_staff= is_staff,
            is_superuser= is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username,email, name, last_name, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username,email, name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length=255, unique= True)
    email = models.EmailField(verbose_name="Email", max_length=255, unique= True)
    name= models.CharField(verbose_name="Name", max_length=255, blank=True, null=True)
    last_name= models.CharField(verbose_name="Last Name", max_length=255, blank=True, null=True)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)


    profile_picture = models.ImageField(verbose_name="Profile Picture", upload_to="services")
    phone_number = models.CharField(verbose_name="Phone number", default=0, max_length=14)
    short_description = models.CharField(verbose_name="Description", max_length=255)
    object= UserManager()

    class Meta:
        verbose_name= "User"
        verbose_name_plural = "Users"

    USERNAME_FIELD ="username"
    REQUIRED_FIELDS = ['email', 'name', 'last_name']


    def __str__(self):
        return f"{self.last_name} {self.name}"

class AnonymousUser(models.Model):
    created_date = models.DateField('Created Date', auto_now=False, auto_now_add=True)
    ip_address= models.GenericIPAddressField()

    class Meta:
        verbose_name= "Anonymous User"
        verbose_name_plural = "Anonymouses Users"

    def __str__(self):
        return f"{self.ip_address} {self.created_date}"


class Room(models.Model):
    created_date = models.DateField('Created Date', auto_now=False, auto_now_add=True)
    anonymousUser = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE,null=True)
    speaker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name= "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f"Creada {self.created_date}/{self.anonymousUser.ip_address}/{self.speaker.username}"