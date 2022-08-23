from django.shortcuts import render

# Create your views here.

def hello(request):
    print("hello world")
    print("Hello Jenkins change test")
    print("This is the testing for learning jenkins")
    return render(request, 'hello.html')
