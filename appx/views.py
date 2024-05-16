from django.shortcuts import render,redirect
from appx.models import contactsave

# Create your views here.
def home(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")
def services(request):
    data=contactsave.objects.all
    return render(request,"services.html",{"all":data})
def delete(request,id):
    data=contactsave.objects.get(id=id)
    data.delete()
    return redirect("services")
def savedata(request):
    if request.method=="POST":
     name=request.POST.get("name")
     email=request.POST.get("email")
     number=request.POST.get("number")
     msg=request.POST.get("msg")
     data=contactsave(name=name,email=email,number=number,msg=msg)
     data.save()
     return redirect("contact")
