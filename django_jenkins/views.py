from django.shortcuts import render

# Create your views here.

def hello(request):
    print("Hello World")
    return render(request, 'hello.html')
