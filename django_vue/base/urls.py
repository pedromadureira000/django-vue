from django.urls import path
from django_vue.base import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
]
