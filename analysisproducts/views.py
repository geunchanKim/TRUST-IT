from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'analysisproducts/analysis.html',
        {
           'posts' : posts,
        }
    )

# Create your views here.
