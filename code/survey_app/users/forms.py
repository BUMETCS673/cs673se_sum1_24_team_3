# code/local_testing_adrian_dnu/myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from surveys.models import Response
from django.forms import modelformset_factory

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['answer']
        widgets = {
            'answer': forms.RadioSelect
        }

ResponseFormSet = modelformset_factory(
    Response,
    fields=('answer',),
    extra=0,
    widgets={'answer': forms.RadioSelect},
)
