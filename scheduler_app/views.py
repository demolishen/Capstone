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

def about(request):
    about_description = {
       'about_message' : "Brianna's Cleaning Business takes pride in being responsible for keeping offices, homes, hotels or other public areas neat and organized. Our main duties include sweeping, mopping and vacuuming floors, dusting counter-tops, ceilings and furniture and sanitizing bathrooms, kitchens or other public areas. Performing routine inspections to check that spaces like restrooms and other living areas are always sanitary."
    }
    return render(request, 'about.html', about_description)

def contact(request):
    contact_description = {
        'contact_description' : "Brianna G, email:email@email.com, Cell: 8675309, Business Address: 404 Yougot It Lane"
    }
    return render(request, 'contact.html', contact_description)
# app_name = 'scheduler_app'
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('schedule')
# ]

class CreateJob(LoginRequiredMixin, CreateView):
    model = ScheduleClean
    template_name = "schedule_clean.html"
    fields = ['full_name', 'phone_number', 'email', 'location_address', 'location_zip', 'location_city', 'location_state', 'location_country', 'date_work_requested']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def BriannasView(request):

    users = ScheduleClean.objects.all()
    context = {"object_list" : users}

    return render(request, 'briannas_page.html', context)