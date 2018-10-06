from django import forms
from django.core import validators
from forms.models import User

class Form_Name(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False , widget=forms.HiddenInput , validators =[validators.MaxLengthValidator(0)])
class NewUser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'