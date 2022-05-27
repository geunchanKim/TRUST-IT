from django.urls import path
from . import views

urlpatterns = [
    path('nokids/', views.Map_Comment_List_Nokids.as_view()),
    path('hospital/', views.Map_Review_List.as_view()),
    path('playground/', views.Map_Comment_List_Playground.as_view())
]