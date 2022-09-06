from urllib import request
from django.shortcuts import render


def all_api_list(request):
    
    context={

    }

    return render(request,'base.html',context)



