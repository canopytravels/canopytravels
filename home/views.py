from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def rent(request):
    return render(request, 'rent.html')