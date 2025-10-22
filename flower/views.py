from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Daisy
# Create your views here.
from django.contrib import messages
from .form import DaisyForm

def flower1(request):
    return render(request, "flower.html")

def get_all(request):
    print('request', request)
    
    flower_list = Daisy.objects.all().order_by("-create_at")
    #print(f"-------**{flower_list}------**")
    if flower_list:
        context = {
            "data": flower_list,
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
        form = DaisyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "update successfully.")
            return redirect("add-items")
        
        messages.error(request, "error adding items")
        return redirect("add-items")

        #title = request.POST.get("title")
        #des = request.POST.get("description")

        #print(title, des)
        #data = Daisy(title=title, description=des)
        #data.save()
        #print("data is save successfully")
        #Daisy.objects.create(title=title,describtion=describtion)
   else:
    form = DaisyForm()
    context = {
            "form": form
        }
    return render (request, "add_items.html",context)


def update(request, id):
    
    try:
      daisy = Daisy.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")
      
    if request.method =="POST":
        
        form = DaisyForm(request.POST, instance=daisy)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Items sucessfully updated")
            
            return redirect("update", id=daisy.id)
        
        messages.error("error updating items")
        return redirect("update", id=daisy.id)
   

    form = DaisyForm(instance=daisy)
    
    context = {
    "id": daisy.id,
    "form": form
    }

    return render(request, "edit_items.html", context)
        
    


def delete(request, id):
      
    try:
      daisy = Daisy.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")
    
    daisy.delete()
    messages.success(request, f"{id} delete successfully")
    return redirect("get-all")
#def home(request):
   # return render(request, "Hello, I'm Aru. I love flowers much more.")
