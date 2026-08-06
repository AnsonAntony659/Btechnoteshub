from django.shortcuts import render
from .models import University
# Create your views here.


def university_list(request):
    universities=University.objects.all()

    context={
        'universities':universities
    }

    return render(request,'universities/university_list.html',context)