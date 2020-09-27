from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksPage.as_view(), name='tasks_page'),
]
