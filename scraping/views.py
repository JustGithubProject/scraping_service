from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    obj = Vacancy.objects.all()
    return render(request, "home.html", {"obj": obj})