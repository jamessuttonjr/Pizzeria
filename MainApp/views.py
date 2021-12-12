from django.shortcuts import render

# Create your views here.

def index (request):
    #Pizzeria Home Page
    return render(request, 'MainApp/index.html')