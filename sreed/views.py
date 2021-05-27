from django.shortcuts import render
from .models import TextLevel
# Create your views here.


def sreedConf(request):
    return render(request, 'sreed/sreedConf.html',)
