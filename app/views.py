from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def topic(request):
    if request.method=='POST':
        to=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=to)[0]
        TO.save()
        return HttpResponse('data is sumitted')

    return render(request,'topic.html')
def webpage(request):
    if request.method=='POST':
        topic=request.POST['to']
        TO=Topic.objects.get(topic_name=topic)
        name=request.POST['name']
        url=request.POST['url']
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('webpage insertion is done')
    return render(request,'webpage.html')
def accessrecord(request):
    if request.method=='POST':
        name=request.POST['name']
        NO=Webpage.objects.get(name=name)
        
        date=request.POST['date']
        author=request.POST['author']
        AO=AccessRecord.objects.get_or_create(name=NO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('Accessrecord is inserted')
    return render(request,'accessrecord.html')