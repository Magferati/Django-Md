from django.shortcuts import render
from django.http import HttpResponse
from .models import Daisy
# Create your views here.

def flower1(request):
    return render(request, "flower.html")

def get_all(request):
    print('request', request)
    
    flower_list = Daisy.objects.all().order_by("title")
    if flower_list:
        context = {
            "date": flower_list,
            "html_title": "....This is my page...."
        }
        return render(request, "flower.html", context)
    
    else:
        return HttpResponse(f"Not available data")
    
def get_data_by_id(request, id):
    print(request,"request")

    flower_list = Daisy.objects.get(id=id)
    if flower_list:
        context = {
            "items": flower_list,
            "html_title": "....This is my page...."
        }
        return render(request, "show_item.html", context)
    
def create(request):
    Daisy.objects.create()

def update(request, id, title, describtion):
    a = Daisy.objects.ger(id=id)

    a.title = title
    a.discribtion = describtion
    a.save()

    return HttpResponse(f"{a.title} and {a.discribtion} updated")
def delete(request, id):
    a = Daisy.objects.get(id=id)
    a.delete()
    return HttpResponse(f"{id} was delete successfully")
#def home(request):
   # return render(request, "Hello, I'm Aru. I love flowers much more.")
