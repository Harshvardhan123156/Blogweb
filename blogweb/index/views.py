from django.shortcuts import render , HttpResponse

def home(request):
    return render(request , 'homee/home.html')