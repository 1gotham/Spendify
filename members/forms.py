from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'class':'form-input',
            'placeholder':'USERNAME',
            'maxlength':'16',
            'minlength':'3',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'class':'form-input',
            'placeholder':'EMAIL',
            'maxlength':'30',
            'minlength':'3',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'class':'form-input',
            'placeholder':'PASSWORD',
            'maxlength':'16',
            'minlength':'3',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'class':'form-input',
            'placeholder':'CONFIRM PASSWORD',
            'maxlength':'16',
            'minlength':'3',
        })     
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']