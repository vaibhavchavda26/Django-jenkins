from django.shortcuts import render

# Create your views here.

def hello(request):
    print("Hello Jenkins")
    return render(request, 'hello.html')
