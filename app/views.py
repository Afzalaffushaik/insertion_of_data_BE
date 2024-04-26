from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from app.models import *

def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic created successfully')

def insert_webpage(request):
    tn=input('enter a tn')
    n=input('enter a name')
    u=input('enter url')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('web page created successfully')
def insert_access(request):

    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter a name')
    u=input('enter a url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input('enter a date')
    a=input('enter a author')
    AO=Access_record.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('access record created successfully')
