from django.http import HttpResponse
from django.shortcuts import render
from .models import Student,Personal
# Create your views here.


def support(request):

    if request.method == 'POST':
        num=request.POST.get('num','')
        name=request.POST.get('name','')
        surname=request.POST.get('surname','')
        Age=request.POST.get('Age','')
        Address=request.POST.get('Address','')
        note=request.POST.get('note','')
        birthdate=request.POST.get('birthdate','')


        if num and name and surname and Age and Address and note and birthdate:
            student=Student(num=num,name=name,surname=surname,Age=Age,Address=Address,note=note,birthdate=birthdate)
            student.save()
        else:
             return HttpResponse("sorry bhava")

    return render(request,'support.html')





def index(request):

    if request.method == 'POST':
        name=request.POST.get('name','')
        birthday=request.POST.get('birthday','')
        gender=request.POST.get('gender','')
        subject=request.POST.get('subject','')
        res_code=request.POST.get('res_code','')


        if name and birthday and gender and subject and res_code :
            personal=Personal(name=name,birthday=birthday,gender=gender,subject=subject,res_code=res_code)
            personal.save()
            return render(request, 'thankyou.html')


        else:
             return render(request,'error.html')

    return render(request,'index.html')


def thankyou(request):
    return render(request,'thankyou.html')

