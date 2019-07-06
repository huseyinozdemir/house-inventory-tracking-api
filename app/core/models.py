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

    def CreateSuperuser(self, email, password=None, **args):
        """Create and Save Superuser"""
        user = self.CreateUser(email, password)
        user.isStaff = True
        user.isSuperuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    isStaff = models.BooleanField(default=True)
    isSuperuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class BuildingManager(models.Manager):

    def CreateBuilding(self, name=None, **args):
        """Create and Save Building"""
        if not name:
            raise ValueError('Buildind must have a name')
        building = self.model(name=name, **args)
        building.save(using=self._db)

        return building


class Building(models.Model):
    """Buildin table"""
    name = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)

    objects = BuildingManager()


class FlatManager(models.Manager):

    def CreateFlat(self, name=None, buildingId=None, **args):
        """Create and Save Flat"""
        if not name:
            raise ValueError('Flat must have a name')
        if not buildingId:
            raise ValueError('Flat must have a building')
        flat = self.model(name=name, buildingId=buildingId, **args)
        flat.save(using=self._db)

        return flat


class Flat(models.Model):
    """Flat table"""
    name = models.CharField(max_length=255)
    buildingId = models.ForeignKey(
        Building,
        on_delete=models.DO_NOTHING
    )
    isDelete = models.BooleanField(default=False)

    objects = FlatManager()


class FixtureManager(models.Manager):

    def CreateFixture(self, name=None, flatId=None, priceValue=None, **args):
        """Create and Save Fixture"""
        if not name:
            raise ValueError('Fixture must have a name')
        if not flatId:
            raise ValueError('Fixture must have a Flat')
        if not priceValue:
            raise ValueError('Fixture must have a Price Value')
        fixture = self.model(name=name, flatId=flatId,
                             priceValue=priceValue, **args)
        fixture.save(using=self._db)

        return fixture


class Fixture(models.Model):
    """Fixture table"""
    name = models.CharField(max_length=255)
    flatId = models.ForeignKey(
        Flat,
        on_delete=models.DO_NOTHING
    )
    isDelete = models.BooleanField(default=False)
    priceValue = models.FloatField(default=0)

    objects = FixtureManager()
