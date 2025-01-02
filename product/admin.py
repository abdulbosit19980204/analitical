from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Product, ProductBrand, ProductSeria, ProductCategory, CategoryMobile, Manufacturer, \
    TypeOfNomenclature, ListGroup, ProductImages, ProductRemainder


class ProductAdmin(ImportExportModelAdmin, ModelAdmin):
    list_display = ('id', 'print_title', 'list_group', 'product_category', 'brand', 'article')
    list_display_links = (
        'id', 'print_title', 'list_group', 'product_category', 'brand', 'article')
    list_filter = ('product_category', 'brand', 'list_group')
    search_fields = ('title', 'description')


# Product's models
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductSeria)
admin.site.register(Manufacturer)
admin.site.register(TypeOfNomenclature)
admin.site.register(ListGroup)
admin.site.register(CategoryMobile)
admin.site.register(ProductImages)
admin.site.register(ProductRemainder)
