from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksPage(View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/tasks_page.html',)


class RatingPage(View):
    login_url = '/signin/'

    def get(self, request):
        return render(request, 'webapp/pages/rating_page.html')
