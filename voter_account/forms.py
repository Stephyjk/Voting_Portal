from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length = 100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}
