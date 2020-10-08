from django import forms

class NameForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=30,widget=forms.EmailInput(attrs={"class":"flow=control"}))
    password=forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput())