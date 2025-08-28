from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, name, email, username, password=None, **extra_fields):
        if not email or not username:
            raise ValueError('The Email and Username fields must be set')
        email = self.normalize_email(email)
        user = self.model(
            name=name, 
            email=email, 
            username=username,
            **extra_fields) 
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
