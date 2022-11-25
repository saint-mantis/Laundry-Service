from django import forms
from .models import *



class userSignupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(userSignupForm, self).__init__(*args, **kwargs)

    class Meta:
        model = userDataModel
        labels = {

        }
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={}),
            'name': forms.TextInput(attrs={}),
            'email': forms.TextInput(attrs={}),
            'password': forms.TextInput(attrs={}),
            'phone': forms.TextInput(attrs={}),
        }

class userLoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(userLoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = userDataModel
        labels = {

        }
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={}),
            'password': forms.TextInput(attrs={}),
        }