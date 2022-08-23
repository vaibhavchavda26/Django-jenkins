from django.shortcuts import render

# Create your views here.

def hello(request):
    print("hello again")
    return render(request, 'hello.html')
