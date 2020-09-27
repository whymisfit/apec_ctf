from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksPage(LoginRequiredMixin, View):
    login_url = '/signin/'
    template_name = 'webapp/tasks_page.html'

    def get(self, request):
        return render(request, self.template_name, )
