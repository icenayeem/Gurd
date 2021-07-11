from django import forms
from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistation
from .models import studentin
#this function is used for show and add data
def addshow(request):
    if request.method == 'POST':
        fm = studentregistation(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pa = fm.cleaned_data['password']
            reg = studentin(name=nm,email=em,password=pa)
            reg.save()
            fm = studentregistation()
            
    else:
        fm = studentregistation()
    
    stud = studentin.objects.all()
    return render(request,'enroll/addshow.html',{'form':fm,'stu':stud})
#this function is used for update data
def update_data(request,my_id):
    if request.method == "POST":
        p = studentin.objects.get(pk=my_id)
        fm = studentregistation(request.POST,instance=p)
        if fm.is_valid():
            fm.save()
    else:
        p = studentin.objects.get(pk=my_id)
        fm = studentregistation(instance=p)
    return render(request,'enroll/updateshow.html',{'form':fm,'pr':p})
#tis function is used for delete data
def delete_data(request,my_id):
    if request.method == 'POST':
        par = studentin.objects.get(pk=my_id)
        par.delete()
        return HttpResponseRedirect('/')
