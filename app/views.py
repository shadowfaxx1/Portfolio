from django.shortcuts import render

# Create your views here.

def home(request):
    print("hi ")
    return render(request,"app/index.html")

def temp(request):
    return render(request,"app/elements.html")

def temp2(request):
    return render(request,"app/generic.html")

def temp3(request):
    return render(request,"app/landing.html")
