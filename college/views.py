from django.shortcuts import render
from college.models import list,details


def index(request):
    cl = list.objects.order_by('rank')
    var = {'ck': cl}
    return render(request ,'index.html',context = var)
