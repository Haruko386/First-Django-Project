from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        return HttpResponse(f'username: {username}, password: {password}')
    elif request.GET:
        return HttpResponse(f'Login Deny')

    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/logout.html')


def profile(request):
    return render(request, 'account/profile.html')


def edit(request):
    return render(request, 'account/edit.html')


class RegisterView(View):

    def get(self, request):
        return render(request, 'account/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        return HttpResponse(
            f'username: {username}, password: {password}, password2: {confirm_password}, email: {email}')
