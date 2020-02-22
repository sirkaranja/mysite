from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.PostList.as_view(), name='home'),
    path('post_detail/', views.PostDetail.as_view(), name='post_detail'),
]