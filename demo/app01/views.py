from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')


def article_create(request):
    return HttpResponse('Successful')


def article_detail(request, article_id):
     return HttpResponse(f'id is {article_id}')


def phone_detail(request, phone_number):
    return HttpResponse(f'The phone number is {phone_number}')
