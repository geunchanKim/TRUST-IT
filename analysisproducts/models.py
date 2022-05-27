from ast import Import
from tabnanny import verbose
from django.db import models
from pickle import TRUE
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/analysisproducts/category/{self.slug}/'

    class Meta:
        verbose_name_plural="Categories"

class Company(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique= True, allow_unicode=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/analysisproducts/company/{self.slug}/'
    
class Product(models.Model):
    title = models.CharField(max_length=30)
    product_img = models.ImageField(upload_to='analysisproducts/images/%Y/%m/%d/', blank=True)
    hook_text = models.CharField(max_length=100, blank=True)
    analysis_content = models.TextField()
    
    company = models.ForeignKey(Company, null=TRUE, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=TRUE, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.company}'

    def get_absolute_url(self):
        return f'/analysisproducts/{self.pk}/'

