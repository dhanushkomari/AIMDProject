from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'AIMDApp/home.html')


