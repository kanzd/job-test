from django import forms
  
class Image(forms.Form):
    tag = forms.CharField()
    image = forms.ImageField()