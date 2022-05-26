from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        #context['categories'] = Category.objects.all()
        # context['no_category_post_count'] = Post.objects.filter(
        #     category=None).count()
        return context