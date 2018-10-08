from django.shortcuts import render
from forms.form import Form_Name , NewUser

def form_name(request):
    form1 = Form_Name()

    if request.method == 'POST':
        form1 = Form_Name(request.POST)
        if form1.is_valid():
            print("NAME : "+form1.cleaned_data['name'])
            print("EMAIL : " + form1.cleaned_data['email'])
            print("TEXT : " + form1.cleaned_data['text'])

    return render(request ,'form.html', context = {'form' : form1})

def users(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR")
    return render(request, 'Msc/user.html', context={'form2': form})
