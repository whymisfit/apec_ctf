from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListPage(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/task_list_page.html', )


class RatingPage(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/rating_page.html')


class TaskPage(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/task_page.html')
