from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scheduler_app/", include('scheduler_app.urls'))
]
