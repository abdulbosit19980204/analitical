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
    fieldsets = (
        ("Main", {'fields': (
            'print_title', 'working_title', 'name_manufacturer', 'brand', 'list_group', 'product_category',
            'project', 'country_of_origin', 'category_mobile', 'type_of_nomenclature', 'keep_custom_declaration',
            'keep_nomenclature_certificates')}),
        (
            'Code info',
            {'fields': ('supplier_code', 'manufacturer_code', 'barcode', 'article', 'hs_code',)}),
        ('Weight and Height info', {'fields': (
            'weight_of_box_net', 'weight_of_orginal_box_net', 'weight_of_box_gross', 'length_of_box', 'box_width',
            'height_of_box', 'box_volume', 'box_area', 'weight_of_packaging_net', 'weight_of_packaging_orginal_net',
            'weight_of_packaging_gross', 'package_length', 'package_width', 'package_height', 'packaging_volume',
            'packaging_area', 'number_of_pieces_in_box', 'storage_unit')}),
        # ('Additional info',
        #  {'fields': ('signboard', 'tradePointType', 'theNumberOfOrders', 'creditLimit', 'accumulatedCredit',)}),
    )


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
