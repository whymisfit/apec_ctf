from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


class SigninPage(View):

    def get(self, request):
        return render(request, 'login/signin.html', )

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().dispatch(request, *args, **kwargs)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request=request, user=user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/signin/')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/signin/')
