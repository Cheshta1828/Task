from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='ID')
    password = forms.CharField(widget=forms.PasswordInput)
