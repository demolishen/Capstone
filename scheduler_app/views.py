from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    data = {
        'message': "Hello World",
    }
    return render(request, 'scheduler_app/main_template.html', data)


