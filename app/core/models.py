from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):

    def CreateUser(self, email, password=None, **args):
        """Create and Save user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **args)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


