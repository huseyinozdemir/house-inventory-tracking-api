from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **args):
        """Create and Save user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **args)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **args):
        """Create and Save Superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class BuildingManager(BaseUserManager):

    def create_building(self, name=None, user=None, **args):
        """Create and Save Flat"""
        if not name:
            raise ValueError('Flat must have a name')
        if not user:
            raise ValueError('Flat must have an user')
        building = self.model(name=name, user=user, **args)
        building.save(using=self._db)

        return building


class Building(models.Model):
    """Buildin table"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    objects = BuildingManager()

    def __str__(self):
        return self.name


class FlatManager(BaseUserManager):

    def create_flat(self, name=None, user=None, building=None, **args):
        """Create and Save Flat"""
        if not name:
            raise ValueError('Flat must have a name')
        if not user:
            raise ValueError('Flat must have an user')
        if not building:
            raise ValueError('Flat must have a building')
        flat = self.model(name=name, user=user, building_id=building, **args)
        flat.save(using=self._db)

        return flat


class Flat(models.Model):
    """Flat table"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    building_id = models.ForeignKey(
        Building,
        on_delete=models.DO_NOTHING
    )

    objects = FlatManager()

    def __str__(self):
        return self.name


class RoomManager(BaseUserManager):

    def create_room(self, name=None, user=None, flat=None, **args):
        """Create and Save Flat"""
        if not name:
            raise ValueError('Flat must have a name')
        if not user:
            raise ValueError('Flat must have an user')
        if not flat:
            raise ValueError('Flat must have a flat')
        flat = self.model(name=name, user=user, flat_id=flat, **args)
        flat.save(using=self._db)

        return flat


class Room(models.Model):
    """Room table"""

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    flat_id = models.ForeignKey(
        Flat,
        related_name='flat',
        on_delete=models.DO_NOTHING
    )

    objects = RoomManager()

    def __str__(self):
        return self.name


class FixtureManager(BaseUserManager):

    def create_fixture(self, name=None, user=None, room=None, **args):
        """Create and Save Fixture"""
        if not name:
            raise ValueError('Fixture must have a name')
        if not user:
            raise ValueError('Fixture must have an user')
        if not room:
            raise ValueError('Fixture must have an room')
        fixture = self.model(name=name, user=user, room_id=room, **args)
        fixture.save(using=self._db)

        return fixture


class Fixture(models.Model):
    """Fixture table"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    room_id = models.ForeignKey(
        Room,
        on_delete=models.DO_NOTHING
    )
    price_value = models.FloatField(default=0)

    objects = FixtureManager()

    def __str__(self):
        return self.name
