from django.shortcuts import render,redirect
from app.models import Info
# Create your views here.
def home(request):
    return render(request,'home.html')

def form(request):
    if request.method=="POST":
        name=request.POST["nm"]
        email=request.POST["em"]
        obj=Info(name=name,email=email)
        obj.save()
        return redirect(message)
    else:
        return render(request,'form.html')

def message(request):
    return render(request,'message.html')