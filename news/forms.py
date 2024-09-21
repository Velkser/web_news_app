from .models import News
from django.forms import TextInput, Textarea, DateTimeInput
from django.forms import ModelForm

class NewsForm(ModelForm):
    
    ...
    
    class Meta:
        model = News
        fields = ["title", "anons", "text", "date"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter title"
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter anons"
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "enter text"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "enter date"
            })
        }



