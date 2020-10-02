from django.urls import path
from . import views


urlpatterns = [
    path('', views.SigninPage.as_view(), name='signin_page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]