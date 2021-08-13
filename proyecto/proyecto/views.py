from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def Primera(request):
    return render(request, 'primera.html')