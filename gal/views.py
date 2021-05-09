from django.shortcuts import render,redirect
from . import forms
# Create your views here.
from . import models
import math

def rendere(req):
    return redirect("images/1")
def base(req,page):
    images=models.Image.objects.all()
    val = math.ceil(len(images)/8)
    print(val)
    return render(req,"images.html",{"type":"normal","images":images[(page-1)*8:page*8],"pages":list(range(1,val+1))})

def getUpload(req):

    return render(req,'upload.html',{"form":forms.Image()})
def search(req,tag,page):
    images = models.Image.objects.filter(tag=tag)
    val = math.ceil(len(images)/8)
    print(val)
    return render(req,"images.html",{"tag":tag,"type":"search","images":images[(page-1)*8:page*8],"pages":list(range(1,val+1))})
def upload(req):
    
    formm = forms.Image(req.POST, req.FILES)
    formm.is_valid()
    tag = formm.cleaned_data.get("tag")
    image = formm.cleaned_data.get("image")

    print(tag,image)
    if tag!="" and image!="":
        img = models.Image()
        img.tag=tag
        img.images=image
        img.save()
    return render(req,"status.html")

        