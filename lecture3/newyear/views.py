from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
        'current_time': now,
        'greeting': 'Happy New Year!' if now.month == 1 and now.day == 1 else 'Welcome!'
    })