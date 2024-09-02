from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models

class SignUpForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email', 'class': 'input'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password', 'class': 'input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm the password', 'class': 'input'})


class SignInForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'input'}))

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter password', 'class': 'input'})
        self.fields['username'].label = "Email"  # Update label to 'Email'