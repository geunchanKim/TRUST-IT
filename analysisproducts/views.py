from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.db.models import Q
   
class ProductList(ListView):
    model= Product
    #ordering = '-pk'
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_product_count'] = Product.objects.filter(
            category=None).count()
        return context

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_product_count'] = Product.objects.filter(
            category=None).count()
        return context 

def category_page(request, slug):
    if slug == 'no_category':
        category ='기타'
        product_list = Product.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        product_list =  Product.objects.filter(category=category)
    
    return render(
        request,
        'analysisproducts/product_list.html',
        {
            'product_list': product_list,
            'categories': Category.objects.all(),
            'no_category_product_count': Product.objects.filter(category=None).count(),
            'category': category,
        }

    )  
class ProductSearch(ProductList):
    paginate_by: None
    
    def get_queryset(self):
        q= self.kwargs['q']
        product_list = Product.objects.filter(
            Q(title__contains=q) | Q(company__name__contains=q)
        ).distinct() #중복 방지
        return product_list
    
    def get_context_data(self, **kwargs):
        context = super(ProductSearch,self).get_context_data()
        q= self.kwargs['q']
        context["search_info"] =f'Search: {q} ({self.get_queryset().count()})' 
        return context
