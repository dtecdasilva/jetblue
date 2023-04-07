from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', 'shipped_from', 'destination', 'shipped_id', 'status')


admin.site.register(Package, PackageAdmin)
