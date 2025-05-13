import os
from app01.views import *
from django.urls import path

urlpatterns = [
    path('create/', article_create, name='article_create'),
    path('detail/<int:article_id>', article_detail, name='article_detail'),

]
