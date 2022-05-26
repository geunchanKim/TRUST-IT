from django.shortcuts import render
from .models import Post

from django.views.generic import ListView
# from .models import Notice

class NoticeListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'notification/indexNotification.html'  #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'notice_list'        #DEFAULT : <model_name>_list

    def get_queryset(self):
        notice_list = Post.objects.order_by('-pk') 
        return notice_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'notification/indexNotification.html',
#         {
#            'posts' : posts,
#         }
#     )

# Create your views here.
