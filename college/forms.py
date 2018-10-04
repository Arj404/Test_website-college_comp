from django import forms
from django.core import validators
from college.models import User

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False , widget=forms.HiddenInput , validators =[validators.MaxLengthValidator(0)])
class NewUser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'