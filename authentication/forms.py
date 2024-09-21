from django import forms
from django.forms import TextInput, PasswordInput, Field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    password1 = Field(
        help_text="password",
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    password2 = Field(
        help_text="confirm password",
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    username = Field(
        help_text="username",
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = Field(
        help_text="username",
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'username'})
    )

    password = Field(
        help_text="password",
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

