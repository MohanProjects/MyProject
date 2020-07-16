from django.shortcuts import render
from testApp.models import *
# Create your views here.
def index(request):
    return render(request,'testApp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/hydjobs.html',context=my_dict)

def bangjobs1(request):
    jobs_list=bangjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/bangjobs.html',context=my_dict)

def chennaijobs1(request):
    jobs_list=chennaijobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/chennaijobs.html',context=my_dict)

def punejobs1(request):
    jobs_list=punejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/punejobs.html',context=my_dict)
