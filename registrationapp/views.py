from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
# Create your views here.





def index(request):

    if request.method == 'POST':
        num=request.POST.get('num','')
        name=request.POST.get('name','')
        surname=request.POST.get('surname','')
        Age=request.POST.get('Age','')
        Address=request.POST.get('Address','')
        note=request.POST.get('note','')

        if num and name and surname and Age and Address and note:
            student=Student(num=num,name=name,surname=surname,Age=Age,Address=Address,note=note)
            student.save()
        else:
             return HttpResponse("sorry bhava")

    return render(request,'index.html')