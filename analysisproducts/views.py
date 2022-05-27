from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product,Company, Category

def category_page(request, slug):
    if slug == 'no_category':
        category ='미분류'
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
def company_page(request, slug):
    company = Company.objects.get(slug=slug)
    product_list = company.post_set.all()

    return render(
        request,
        'analysisproducts/product_list.html',
        {
            'product_list': product_list,
            'company': company,
        }
    )
        
class ProductList(ListView):
    model= Product
    #ordering = '-pk'
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        return context

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        
        return context 

# Create your views here.
