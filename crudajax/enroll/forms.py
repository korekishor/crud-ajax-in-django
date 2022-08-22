from dataclasses import field
from tkinter import Widget
from .models import User
 
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        Widget={
            'name':forms.TextInput(attrs={'class':'form-control',id:'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control',id:'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control',id:'passwordid'})
        }
