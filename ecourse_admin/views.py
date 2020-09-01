from django.shortcuts import render,HttpResponse
from .models import addcourse as readcour;
from django.template.defaulttags import register
# One-time configuration and initialization.
import json 

def courses():
    data=readcour.objects.all()
    res={}
    j=0
    for i in data:
        res[j]={
          "title":i.title,
          "id":i.id
        }
        j +=1
    return res

def index(request):
    return render(request , 'index.html')


def dashboard(request):
    data=courses()
    if data != {}:
        contex={
         "data":data,
         "mode":"courses"
        }
        return render( request , 'admin_addcourse.html',contex);

def addcourse(request,mode):
    data=courses()
    if data != {}:
        data['mode']=mode
        data["data"]=data
        return render( request , 'admin_addcourse.html', data);


def profile(request):
    return render(request , 'admin_profile.html')


def settings(request):
    return render(request ,'admin_settings.html')


def uploadvideos(request ,id):
    ids ={
      "id":id,
    }
    return render(request ,'uploadvideos.html',ids)


def logout(request):
    return HttpResponse('from logout')