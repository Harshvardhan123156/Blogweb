from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact

def home(request):
    return HttpResponse("hey this if the infrmation section.")

def about(request):
    return render(request , 'info/about.html')

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5 :
            messages.error(request , "There is some mistake in the input you gave!!")
        else:
            messages.success(request, "Your query has been passed to us!")
            contact = Contact(name=name , email=email , phone=phone ,content=content)
            contact.save()
    return render(request , 'info/contact.html')
# Create your views here.
