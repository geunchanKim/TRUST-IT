from django.contrib import admin

# Register your models here.
from .models import News, Category, Tag
admin.site.register(News)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
