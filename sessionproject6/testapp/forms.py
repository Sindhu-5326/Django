from django import forms

class NameForm(forms.Form):
    name=forms.CharField()

class AgeForm(forms.Form):
    age=forms.IntegerField()

class GfForm(forms.Form):
    # Define your form fields here
    gf = forms.CharField(max_length=100)






