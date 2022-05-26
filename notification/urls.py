from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoticeListView.as_view(), name='notice_list'),
]
