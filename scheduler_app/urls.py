from django.urls import path
from . import views

app_name = "scheduler_app"
urlpatterns = [
    path('', views.home, name='home'),
    path('scheduler_app/schedule_clean/', views.CreateJob.as_view(), name='new_job'),
    path('scheduler_app/briannas_page/', views.BriannasView, name='briannas_page')

]