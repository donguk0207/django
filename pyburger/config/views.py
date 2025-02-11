from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def index(request):
    return render(request, template_name="main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    return render(request, "burger_list.html", {"burgers": burgers})

def burger_search(request):
    #keyword = request.GET["keyword"]
    keyword = request.GET.get("keyword", None)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()

    return render(request, "burger_search.html", {"burgers": burgers})