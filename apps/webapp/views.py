from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class TaskListPage(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        context = {
            "tasks": Task.objects.all(),
            "categories": Category.objects.all(),
            "team": Profile.objects.get(user=request.user).team,
        }
        return render(request, 'webapp/pages/task_list_page.html', context)


class RatingPage(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request):
        context = {
            "teams": Team.objects.all().order_by("-score"),
        }
        return render(request, 'webapp/pages/rating_page.html', context)


class TaskPage(LoginRequiredMixin, View):
    login_url = '/signin/'

    def get(self, request, task_id):
        context = {
            "task": Task.objects.get(id=task_id),
            "team": Profile.objects.get(user=request.user).team,
        }
        return render(request, 'webapp/pages/task_page.html', context)
