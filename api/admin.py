from django.contrib import admin
from .models import UserType, CustomUser, KPI, Project, Warehouse, Organization
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
    list_display = ('id', 'name', 'description')
    inlines = [Organization, ]


class CustomUserAdmin(UserTypeAdmin):
    list_display = ('id', 'username', 'email', 'first_name',)


admin.site.register(UserType, UserTypeAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(KPI)
admin.site.register(Project)
admin.site.register(Warehouse)
admin.site.register(Organization)

# ********************** unregistred*************
admin.site.unregister(Group)
