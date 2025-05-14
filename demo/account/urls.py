from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]