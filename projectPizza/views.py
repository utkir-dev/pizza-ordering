from django.shortcuts import render
from projectPizza.models import Pizza,PizzaNumber
# Create your views here.

def home(request):
    pizza=Pizza.objects.all()[:6] 
    pizza_number=PizzaNumber.objects.all()
    context={
        'pizza':pizza,
        'pizza_number':pizza_number,
        
        }
    return render(request,'index.html',context)

def menu(request):
    pizza=Pizza.objects.all()[:8] 
    context={'pizza':pizza}
    return render(request,'menu.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')


