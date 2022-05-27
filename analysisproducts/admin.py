from django.contrib import admin

from .models import Company, Product, Category 

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}

     
admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company,CompanyAdmin)