from django.shortcuts import render
from college.models import list,details, User
from . import forms


def index(request):
    cl = list.objects.order_by('rank')
    var = {'ck': cl}
    return render(request ,'index.html',context = var)

def form_name(request):
    form1 = forms.FormName()

    if request.method == 'POST':
        form1 = forms.FormName(request.POST)
        if form1.is_valid():
            print("NAME : "+form1.cleaned_data['name'])
            print("EMAIL : " + form1.cleaned_data['email'])
            print("TEXT : " + form1.cleaned_data['text'])

    return render(request ,'form.html', context = {'form' : form1})

def users(request):
    form = User()

    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR")
    return render(request, 'user.html', context={'form2': form})