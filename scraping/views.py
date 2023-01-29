from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now()
    context = {
        "date": date
    }
    return render(request, "home.html", context=context)
