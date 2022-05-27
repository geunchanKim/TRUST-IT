from django.contrib import admin

from .models import Company, Product 

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}

     
admin.site.register(Product)
admin.site.register(Company,CompanyAdmin)