from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Daisy
# Create your views here.

def flower1(request):
    return render(request, "flower.html")

def get_all(request):
    print('request', request)
    
    flower_list = Daisy.objects.all().order_by("create_at")
    print(f"-------**{flower_list}------**")
    if flower_list:
        context = {
            "date": flower_list,
            "html_title": "....This is my page...."
        }
        return render(request, "flower.html", context)
    
    else:
        return HttpResponse(f"No data found")
    
def get_data_by_id(request, id):
    print("request",request)

    flower_list = Daisy.objects.get(id=id)
    if flower_list:
        context = {
            "items": flower_list,
            "html_title": "....This is my page...."
        }
        return render(request, "show_item.html", context)
    
def create (request):
   
   if request.method == "POST":
   
        title = request.POST.get("title")
        des = request.POST.get("description")

        print(title, des)
        data = Daisy(title=title, description=des)
        data.save()
        print("data is save successfully")
        #Daisy.objects.create(title=title,describtion=describtion)
        return redirect("get-all")
   return render (request, "add_items.html")


def update(request, id):
    daisy = Daisy.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        des = request.POST.get("description")

        daisy.title = title
        daisy.description = des
        daisy.save()
        return redirect("get-all")
    context = {
        "id" : daisy.id,
        "title": daisy.title,
        "description":daisy.description
    }

    return render(request, "edit_items.html", context)


def delete(request, id):   
    a = Daisy.objects.get(id=id)
    a.delete()
    return HttpResponse(f"{id} was delete successfully")
#def home(request):
   # return render(request, "Hello, I'm Aru. I love flowers much more.")
