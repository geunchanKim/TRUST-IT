from django.shortcuts import render
#from .models import Post

# Create your views here.

def post_list(request):
    
    return render(
        request,
        'communication/post_list.html',
        # {
        #     'posts' : posts,
        # }
    )