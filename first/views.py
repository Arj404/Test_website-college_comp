from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    var = {'insert_me':"im from veiws.py"}
    return render(request,'index.html',context = var)


# Create your views here.
