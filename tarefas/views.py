from django.shortcuts import render

# Create your views here.

def index(request):
    print("Conseguir chegar na bios")
    return render(request, "index.html")