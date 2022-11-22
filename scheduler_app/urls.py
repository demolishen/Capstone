from django.urls import path
from . import views

app_name = "scheduler_app"
urlpatterns = [
    path('base/', views.base, name='base')
]