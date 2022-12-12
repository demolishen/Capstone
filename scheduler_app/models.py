from django.db import models
from django.urls import reverse



class ScheduleClean(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    location_address = models.CharField(max_length=100)
    location_zip = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_country = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_work_requested = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    in_progress = models.BooleanField(default = False)
    # work_images = models.




    def __str__(self):
        return f'{self.full_name} - {self.location_address}'

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('scheduler_app:home')

