from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''manage profil of the user'''
    def create_user(self, email, name, password=None):
        '''create a new user profil'''
        if not email:
            raise ValueError('user must have email adress')
        email = self.normalize_email(email)
        user =self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''CREATE SUPER USER WITH GIVEN DETAILS'''
        user = self.create_superuser(email ,name, password)

        user.is_active = True
        user.is_staff = True
        user.save(self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''database model fir user in the system'''
    email = models.EmailField(max_length=225 ,unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD ='name'

    def get_full_name(self):
        '''retrive full name of the user'''
        return self.name

    def get_short_name():
        '''retrive short name of the user'''
        return self.name

    def __str__(self):
        '''return string representation  of the user'''
        return self.email
