from django.shortcuts import render

# Create your views here.
import datetime
current_time  = datetime.datetime.now()

def index(request):
    context = {
        "large_number": 98766545565,
        "message": "welcome",
        "current_time": current_time,
        "number":3,
        "day1": current_time + datetime.timedelta(days=200),
        "day2": current_time - datetime.timedelta(days=100),
    }
    return render(request, "humanize_example/index.html", context)