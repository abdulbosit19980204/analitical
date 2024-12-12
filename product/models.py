from django.db import models
from api.models import BaseField, Project, Warehouse, Country
from .external_func import product_image_upload_path


class ProductBrand(BaseField, models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductSeria(BaseField, models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductCategory(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Manufacturer(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ListGroup(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CategoryMobile(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TypeOfNomenclature(BaseField, models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(BaseField, models.Model):
    # ForeignKey fields start
    name_manufacturer = models.CharField(max_length=100, blank=True, null=True)
    list_group = models.ForeignKey(ListGroup, on_delete=models.SET_NULL, null=True)
    working_title = models.CharField(max_length=100, blank=True, null=True)
    print_title = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    supplier_code = models.CharField(max_length=100, blank=True, null=True)
    manufacturer_code = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    article = models.CharField(max_length=100, blank=True, null=True)
    hs_code = models.CharField(max_length=100, blank=True, null=True)
    country_of_origin = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    gost = models.CharField(max_length=100, blank=True, null=True)
    weight_of_box_net = models.FloatField(blank=True, null=True)
    weight_of_orginal_box_net = models.FloatField(blank=True, null=True)
    weight_of_box_gross = models.FloatField(blank=True, null=True)
    length_of_box = models.FloatField(blank=True, null=True)
    box_width = models.FloatField(blank=True, null=True)
    height_of_box = models.FloatField(blank=True, null=True)
    box_volume = models.FloatField(blank=True, null=True)
    box_area = models.FloatField(blank=True, null=True)
    weight_of_packaging_net = models.FloatField(blank=True, null=True)
    weight_of_packaging_orginal_net = models.FloatField(blank=True, null=True)
    weight_of_packaging_gross = models.FloatField(blank=True, null=True)
    package_length = models.FloatField(blank=True, null=True)
    package_width = models.FloatField(blank=True, null=True)
    package_height = models.FloatField(blank=True, null=True)
    packaging_volume = models.FloatField(blank=True, null=True)
    packaging_area = models.FloatField(blank=True, null=True)
    number_of_pieces_in_box = models.PositiveIntegerField(blank=True, null=True)
    storage_unit = models.CharField(max_length=15, blank=True, null=True)
    category_mobile = models.ForeignKey(CategoryMobile, on_delete=models.SET_NULL, null=True)
    type_of_nomenclature = models.ForeignKey(TypeOfNomenclature, on_delete=models.SET_NULL, null=True)
    keep_custom_declaration = models.BooleanField(default=False)
    keep_nomenclature_certificates = models.BooleanField(default=False)

    def __str__(self):
        return self.print_title


class ProductImages(BaseField, models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    # image = models.ImageField(upload_to="images/products/%Y/%m/%d")
    image = models.ImageField(upload_to=product_image_upload_path)

    def __str__(self):
        return self.product.print_title


class ProductRemainder(BaseField, models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    Have = models.PositiveIntegerField(blank=True, null=True)
    Reserved = models.PositiveIntegerField(blank=True, null=True)
    Aviable = models.PositiveIntegerField(blank=True, null=True)
    CodeProduct = models.CharField(max_length=100, blank=True, null=True)
    CodeProject = models.CharField(max_length=100, blank=True, null=True)
    CodeSklad = models.CharField(max_length=100, blank=True, null=True)
    NameProduct = models.CharField(max_length=100, blank=True, null=True)
    dtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.NameProduct
