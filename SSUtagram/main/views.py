from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Feed

# Create your views here.
def home(request):
    feeds=Feed.objects.all()
    return render(request, 'home.html',{'feeds':feeds})

def detail(request, feed_id ):
    feed=get_object_or_404(Feed,pk=feed_id)
    return render(request,'detail.html',{'feed':feed})

def new(request):
    return render(request,'new.html')

def create(request):
    new_Feed=Feed()
    new_Feed.pub_date=timezone.datetime.now()
    new_Feed.text=request.POST['text']
    new_Feed.image= request.FILES['image']
    new_Feed.save()
    return redirect('home')