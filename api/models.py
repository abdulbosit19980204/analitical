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

    class Meta:
        ordering = ['code']


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

    class Meta:
        ordering = ['code']


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

    class Meta:
        # pass
        ordering = ['-date_joined', '-last_login']


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


class Client(BaseField, models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=30)
    signboard = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=100, blank=True, null=True)
    adressDelivery = models.CharField(max_length=300, blank=True, null=True)
    referencePoint = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    contactPerson = models.CharField(max_length=100, blank=True, null=True)
    contactPersonPhone = models.CharField(max_length=100, blank=True, null=True)
    responsiblePerson = models.CharField(max_length=100, blank=True, null=True)
    responsiblePersonPhone = models.CharField(max_length=100, blank=True, null=True)
    tradePointType = models.CharField(max_length=100, blank=True, null=True)
    theNumberOfOrders = models.CharField(max_length=100, blank=True, null=True)
    creditLimit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    accumulatedCredit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    codeRegion = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    mfo = models.CharField(max_length=100, blank=True, null=True)
    bankAccount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Order(BaseField, models.Model):
    agent = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    numOrder = models.CharField(max_length=20)
    dateOrder = models.DateTimeField(blank=True, null=True)
    captionOrder = models.CharField(max_length=100, blank=True, null=True)
    typePrice = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    commentSupervisor = models.TextField(blank=True, null=True)
    commentForwarder = models.TextField(blank=True, null=True)
    commentAgent = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    clientCode = models.CharField(max_length=100, blank=True, null=True)
    clientName = models.CharField(max_length=100, blank=True, null=True)
    codeOrg = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.captionOrder

    class Meta:
        ordering = ['-dateOrder']


class OrderDetail(BaseField, models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    numOrder = models.CharField(max_length=20, blank=True, null=True)
    Credit = models.BooleanField(default=False)
    CodePrice = models.CharField(max_length=100, blank=True, null=True)
    DateOrder = models.DateTimeField(blank=True, null=True)
    CodeSklad = models.CharField(max_length=100, blank=True, null=True)
    CommentSupervisor = models.CharField(max_length=100, blank=True, null=True)
    CommentForwarder = models.CharField(max_length=100, blank=True, null=True)
    CommentAgent = models.CharField(max_length=100, blank=True, null=True)
    ShippingDate = models.DateTimeField(blank=True, null=True)
    OrderType = models.CharField(max_length=100, blank=True, null=True)
    CodeOrg = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.numOrder


class OrderProductRows(BaseField, models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    CodeProduct = models.CharField(max_length=100, blank=True, null=True)
    NameProduct = models.CharField(max_length=100, blank=True, null=True)
    Amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    Price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    Total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    DiscountRate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    Weight = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    Capacity = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    def __str__(self):
        return self.NameProduct


class OrderCreditDetailsList(BaseField, models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    DateOfPayment = models.DateTimeField(blank=True, null=True)
    Total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.order.numOrder


# from api.models import
class Todo(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class VisitingImages(BaseField, models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/visiting_images')

    def __str__(self):
        return self.title


class Country(BaseField, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
