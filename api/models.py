from django.db import models
from django.contrib.auth.models import AbstractUser, User


class BaseField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserType(BaseField, models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Organization(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Warehouse(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    tg_username = models.CharField(max_length=20, unique=True, null=True, blank=True)
    tg_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    picture = models.ImageField(upload_to='images/profile_pictures', default='images/profile_pictures/default.webp')
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)

    c1_connected = models.BooleanField(default=False)
    type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)
    codeProject = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    codeSklad = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class KPI(BaseField, models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    totalFact = models.DecimalField(max_digits=5, decimal_places=2)
    totalPercent = models.DecimalField(max_digits=5, decimal_places=2)
    totalForecast = models.DecimalField(max_digits=5, decimal_places=2)
    totalPercentForecastFact = models.DecimalField(max_digits=5, decimal_places=2)
    okb = models.PositiveIntegerField()
    akbPlan = models.PositiveIntegerField()
    akbFact = models.PositiveIntegerField()
    akbPercent = models.DecimalField(max_digits=5, decimal_places=2)


class Nomenklatura(BaseField, models.Model):
    artikul = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
