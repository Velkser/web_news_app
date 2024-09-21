from django import forms

class DeeplForm(forms.Form):
    target_language = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Target Language'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Text'}))