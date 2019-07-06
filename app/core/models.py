from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


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


class BuildingManager(models.Manager):

    def create_building(self, name=None, **args):
        """Create and Save Building"""
        if not name:
            raise ValueError('Buildind must have a name')
        building = self.model(name=name, **args)
        building.save(using=self._db)

        return building


class Building(models.Model):
    """Buildin table"""
    name = models.CharField(max_length=255)
    is_delete = models.BooleanField(default=False)

    objects = BuildingManager()


class FlatManager(models.Manager):

    def create_flat(self, name=None, building_id=None, **args):
        """Create and Save Flat"""
        if not name:
            raise ValueError('Flat must have a name')
        if not building_id:
            raise ValueError('Flat must have a building')
        flat = self.model(name=name, building_id=building_id, **args)
        flat.save(using=self._db)

        return flat


class Flat(models.Model):
    """Flat table"""
    name = models.CharField(max_length=255)
    building_id = models.ForeignKey(
        Building,
        on_delete=models.DO_NOTHING
    )
    is_delete = models.BooleanField(default=False)

    objects = FlatManager()


class FixtureManager(models.Manager):

    def create_fixture(self, name=None, flat_id=None, price_value=None,
                       **args):
        """Create and Save Fixture"""
        if not name:
            raise ValueError('Fixture must have a name')
        if not flat_id:
            raise ValueError('Fixture must have a Flat')
        if not price_value:
            raise ValueError('Fixture must have a Price Value')
        fixture = self.model(name=name, flat_id=flat_id,
                             price_value=price_value, **args)
        fixture.save(using=self._db)

        return fixture


class Fixture(models.Model):
    """Fixture table"""
    name = models.CharField(max_length=255)
    flat_id = models.ForeignKey(
        Flat,
        on_delete=models.DO_NOTHING
    )
    is_delete = models.BooleanField(default=False)
    price_value = models.FloatField(default=0)

    objects = FixtureManager()
