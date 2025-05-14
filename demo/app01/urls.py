import os
from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.article_create, name='article_create'),
    path('detail/<int:article_id>', views.article_detail, name='article_detail'),
    path('list/', views.article_list, name='article_list'),
]
