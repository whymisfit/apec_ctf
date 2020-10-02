from django.conf.urls.static import static
from django.urls import path
from apec_ctf import settings

from . import views

urlpatterns = [
    path('', views.TaskListPage.as_view(), name='tasks_page'),
    path('rating/', views.RatingPage.as_view(), name='rating_page'),
    path('task/<task_id>', views.TaskPage.as_view(), name='task_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
