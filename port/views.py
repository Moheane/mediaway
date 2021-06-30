from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request, 'port/home.html')
def aboutView(request):
    return render(request, 'port/about.html')
    