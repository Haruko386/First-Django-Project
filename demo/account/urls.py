from django.urls import path
from django.views import View
from . import views
from account.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]