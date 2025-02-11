from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def index(request):
    print("index")
    return render(request, template_name="main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)
    data = {
        "burgers": burgers,
    }

    return render(request, template_name="burger_list.html", context=data)