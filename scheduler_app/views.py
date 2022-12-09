from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import path
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import views
from .models import ScheduleClean

def home(request):
    data = {
        'message': "Hello World",
    }
    return render(request, 'main_template.html', data)

# app_name = 'scheduler_app'
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('schedule')
# ]

class CreateJob(LoginRequiredMixin, CreateView):
    model = ScheduleClean
    template_name = "schedule_clean.html"
    fields = ['full_name', 'phone_number', 'location_address', 'location_zip', 'location_city', 'location_state', 'location_country']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def BriannasView(request):

    users = ScheduleClean.objects.all()
    context = {"object_list" : users}

    return render(request, 'briannas_page.html', context)