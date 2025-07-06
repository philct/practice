from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html', {
        'greeting': 'Hello, world!'
    })

def greet(request, name):
    return render(request, 'hello/greet.html', {
        'greeting': name.capitalize()
    })