from django.shortcuts import render

# Create your views here.

def hello(request):
    print("hello world")
    print("Hello Jenkins")
    return render(request, 'hello.html')
