from django.contrib import admin
from .models import *


class JobTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JobType._meta.fields]

    class Meta:
        model = JobType

admin.site.register(JobType,JobTypeAdmin)


class CompanyJobInline(admin.TabularInline):
    model = Job
    extra = 0

admin.site.register(Job)


class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompanyCategory._meta.fields]

    class Meta:
        model = CompanyCategory

admin.site.register(CompanyCategory,CompanyCategoryAdmin)


class CompaniesAdmin(admin.ModelAdmin):
    inlines = [CompanyJobInline]

    class Meta:
        model = Companies

admin.site.register(Companies, CompaniesAdmin)


