from re import L
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView # CBV
from .models import Map_Comment_Nokids, Map_Review, Map_Comment_Playground
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
# Create your views here.

class Map_Comment_List_Nokids(ListView):
    model = Map_Comment_Nokids
    ordering = '-pk'

    def get_context_data(self,**kwargs): #카테고리 받아오는 과정
        context = super(Map_Comment_List_Nokids,self).get_context_data()
        return context

class Map_Review_List(ListView):
    model = Map_Review
    ordering = '-pk'

class Map_Comment_List_Playground(ListView):
    model = Map_Comment_Playground
    ordering = '-pk'
