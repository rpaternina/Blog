from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from user.models import Profile
User = get_user_model()

class SignUpForm(UserCreationForm):

    username = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    full_name = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre y apellido'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        ]

class LoginForm(AuthenticationForm):

    username = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=None, label='Nombre de usuario')
    full_name = forms.CharField(help_text=None, label='Nombre y apellido')
    email = forms.EmailField(label='Correo')


    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(label='Foto', help_text=None, required=False, widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = [
            'photo',
        ]

class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Contrase??a antigua'}))
    new_password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contrase??a'}))
    new_password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contrase??a'}))

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]