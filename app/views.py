from django.shortcuts import render

# Create your views here.
from app.models import *
def dis_topic(request):
    topics=Topic.objects.all()
    return render(request,'dis_topic.html',context={'topics':topics})

def dis_webpage(request):
    webpages=webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'dis_webpage.html',context=d)

def dis_records(request):
    records=Access_records.objects.all()
    e={'records':records}
    return render(request,'dis_records.html',context=e)
