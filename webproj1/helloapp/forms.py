from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=30, required=True)
    password = forms.CharField(label='password', max_length=30, required=True, widget=forms.PasswordInput())
    passwordconf = forms.CharField(label='passwordconf', max_length=30, required=True, widget=forms.PasswordInput())
    email = forms.CharField(label='email', max_length=30, required=True)
    first_name = forms.CharField(label='first_name', max_length=30, required=True)
    last_name = forms.CharField(label='last_name', max_length=30, required=True)