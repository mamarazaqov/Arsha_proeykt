import datetime

from django.shortcuts import render
from myfiles.models import *
# Create your views here.
def index(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojat(ism=name,email=email,sub=subject,text=msg,date=vaqt).save()

    port = Portfolio.objects.all()
    ports = Jamoa.objects.all()
    pt = Servis.objects.all()
    return render(request,'index.html',{'works':port,'wk':ports,'wks':pt})

def portifilyo_detalis(request,id):
    port = Portfolio.objects.get(id=id)
    return render(request,'portfolio-details.html',{'work':port})