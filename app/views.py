from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *



#Returning String as response by using FBV
def fbv(request):
    return HttpResponse('<h1>This is String on Function based Views')

#Returning String as response by using CBV
class cbv(View):
    def get(self,request):
        return HttpResponse('<h1>This is String on Class based Views')

#Rendering Html Page By FBV
def fbv_html(request):
    return render(request,'fbv_html.html')


#Rendering Html Page By CBV
class csv_html(View):
    def get(self,request):
        return render(request,'csv_html.html')
    
#Data Inserted Through Model Form
    
def insert_school_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Insert Successfully')
    return render(request,'insert_school_fbv.html',d)


class insert_school_cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_school_cbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Insert Successfully')
        

class Cbv_template(TemplateView):
    template_name='Cbv_template.html'