from django import forms

class GiveNumber_form(forms.Form):
    num1 = forms.DecimalField(label="num1")
    num2 = forms.DecimalField(label="num2")
