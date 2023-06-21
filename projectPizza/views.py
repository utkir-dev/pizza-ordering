from django.shortcuts import render,get_object_or_404
from projectPizza.models import Pizza,PizzaNumber,Category,Chef
# Create your views here.

def home(request):
    pizza=Pizza.objects.all().order_by('-id')[:6]
    pizza_number=PizzaNumber.objects.all()
    categories=Category.objects.all()
    context={
        'pizza':pizza,
        'pizza_number':pizza_number,
        'categories':categories,
        }
    return render(request,'index.html',context)

def menu(request):
    pizza=Pizza.objects.all().order_by('-id')[:6]
    context={'pizza':pizza}
    return render(request,'menu.html',context)

def about(request):
    pizza=Pizza.objects.all().order_by('-id')[:6]
    chef=Chef.objects.all().order_by('-id')
    pizza_number=PizzaNumber.objects.all()
    context={
        'pizza_number':pizza_number,
        'pizza':pizza,
        'chef':chef

        }

    return render(request,'about.html',context)

def services(request):
    pizza=Pizza.objects.all()[:6]
    context={
        'pizza':pizza,
                }
    return render(request,'services.html',context)

def contact(request):
    return render(request,'contact.html')

def pizza_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()[:4]
    pizza=Pizza.objects.all()

    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        pizza=pizza.filter(category=category)[:6]

    context={
            'pizza':pizza,
            'category':category,
            'categories':categories
        }
    return render(request,'index.html',context)


def pizza_detail(request,id,slug):
    pizza=get_object_or_404(Pizza,id=id,slug=slug)

    context={
        'pizza':pizza
    }
    return render(request,'pizza_detail.html',context)


