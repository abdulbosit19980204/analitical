from django.contrib import admin
from .models import UserType, CustomUser, KPI, Project, Warehouse, Organization, Client, Order, \
    OrderDetail, Todo, VisitingImages, OrderCreditDetailsList, OrderProductRows, Country, Aksiya
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin


class UserTypeInline(admin.TabularInline):
    model = UserType


class UserTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class KPIAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class OrganizationInline(admin.TabularInline):
    model = Organization


class OrganizationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class ProjectInline(admin.TabularInline):
    model = Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    inlines = [OrganizationInline, ]


class WarehouseInline(admin.TabularInline):
    model = Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'description')
    list_display_links = ('id', 'name')
    list_filter = ('organization',)


class CustomUserAdmin(UserTypeAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'code', 'phone_number', 'tg_username')
    list_display_links = ('id', 'username')


class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'agent', 'client', 'numOrder', 'dateOrder')
    list_display_links = ('id', 'agent', 'client', 'numOrder')
    list_filter = ('agent_id', 'agent',)


class OrderDetailAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'order', 'numOrder', 'CodeSklad', 'ShippingDate')
    list_display_links = ('order', 'id',)
    list_filter = ('CodeSklad', 'ShippingDate', 'created_at', 'updated_at')


class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'inn', 'mfo', 'codeRegion')
    list_display_links = ('id', 'name', 'code')
    list_filter = ('codeRegion',)
    search_fields = ('name', 'inn', 'contactPersonPhone', 'codeRegion')


admin.site.register(UserType, UserTypeAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(KPI)
admin.site.register(Project)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Organization)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Todo)
admin.site.register(VisitingImages)
admin.site.register(OrderCreditDetailsList)
admin.site.register(OrderProductRows)
admin.site.register(Country)
admin.site.register(Aksiya)
# ********************** unregistred*************
admin.site.unregister(Group)
