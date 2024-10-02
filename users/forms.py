from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

'''Данная форма делается для проверок на валидность(длинна пароля, спец символы и тд)'''


class UserLoginForm(AuthenticationForm):

    # username = forms.CharField(
    #     label='Имя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                            'class': 'form-control',
    #                                   'placeholder': 'Введите ваше имя пользователя'})
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={"autofocus": True,
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введите ваш пароль'})
    # )

    class Meta:
        model = User
        fields = ['username',
                  'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        )
