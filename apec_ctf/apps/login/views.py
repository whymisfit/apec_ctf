from django.shortcuts import render
from django.views import View


class SigninPage(View):
    template_name = 'login/signin.html'

    def get(self, request):
        return render(request, self.template_name, )
