from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Feed
# Create your views here.
def home(request):
    feeds=Feed.objects.all()
    return render(request, 'home.html',{'feeds':feeds})

def detail(request, feed_id ):
    feed=get_object_or_404(Feed,pk=feed_id)
    return render(request,'detail.html',{'feed':feed})