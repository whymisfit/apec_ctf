from django.urls import path
from . import views

urlpatters = [
    path('', views.TasksPage.as_view(), name='tasks_page'),
]