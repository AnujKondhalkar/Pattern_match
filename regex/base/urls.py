from django.urls import path
from .import views

urlpatterns = [
    path('', views.regex, name='task_regex'),
]
