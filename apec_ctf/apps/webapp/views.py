from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListPage(View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/task_list_page.html', )


class RatingPage(View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/rating_page.html')


class TaskPage(View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/task_page.html')
