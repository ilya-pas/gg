from django.contrib.auth.forms import UserChangeForm, UserCreationForm, BaseUserCreationForm
from django.contrib.auth.models import Group, User
from .models import Polzovateli, VidSporta, Uprajneniya, Harakteristiki, HarakterisSporta, EtolonRostVes
from django.forms import ModelForm, TextInput, Select, PasswordInput, Textarea, DateTimeInput, CharField, MultipleChoiceField, SelectMultiple

class myUserCreationForm(UserCreationForm):
    password1 = CharField(
        label='Password',
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )
    password2 = CharField(
        label='Password',
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'})
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль',
            })
        }

class myUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'groups']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            }),
            "groups": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            })
        }


class PolzovateliForm(ModelForm):
    class Meta:
        model = Polzovateli
        fields = ['ID_kategorii', 'login', 'parol']

        widgets = {
            "ID_kategorii": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория пользователя',
            }),
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "parol": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }

class VidSportaForm(ModelForm):
    class Meta:
        model = VidSporta
        fields = ['nazvanie_vida', 'opisanie', 'etalon_sila', 'etalon_vinos', 'etalon_skorost', 'etalon_gibkost', 'etalon_koord']

        widgets = {
            "nazvanie_vida": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вида спорта'
            }),
            "opisanie": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание вида спорта'
            }),
            "etalon_sila": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Эталонная сила'
            }),
            "etalon_vinos": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Эталонная выносливость'
            }),
            "etalon_skorost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Эталонная скорость'
            }),
            "etalon_gibkost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Эталонная гибкость'
            }),
            "etalon_koord": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Эталонная координация'
            })
        }

class UprajneniyaForm(ModelForm):
    class Meta:
        model = Uprajneniya
        fields = ['id_harakter','uprajnen', 'pravila_vipolnen', 'vozrast', 'pol', 'normativ_na_6', 'normativ_na_5', 'normativ_na_4', 'normativ_na_3']

        widgets = {
            "id_harakter": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Характеристика'
            }),
            "uprajnen": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Упражнение'
            }),
            "pravila_vipolnen": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Правила выполнения'
            }),
            "vozrast": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "pol": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пол'
            }),
            "normativ_na_6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Норматив на 6'
            }),
            "normativ_na_5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Норматив на 5'
            }),
            "normativ_na_4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Норматив на 4'
            }),
            "normativ_na_3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Норматив на 3'
            })
        }

class HarakteristikiForm(ModelForm):
    class Meta:
        model = Harakteristiki
        fields = ['nazvanie_harakteristiki', 'opisanie_harakteristiki']

        widgets = {
            "nazvanie_harakteristiki": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название характеристики'
            }),
            "opisanie_harakteristiki": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание характеристики'
            })
        }

class HarakterisSportaForm(ModelForm):
    class Meta:
        model = HarakterisSporta
        fields = ['ID_vida_sporta', 'ID_harakter']

        widgets = {
            "ID_vida_sporta": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Название вида спорта'
            }),
            "ID_harakter": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Характеристика'
            })
        }

class EtolonRostVesForm(ModelForm):
    class Meta:
        model = EtolonRostVes
        fields = ['vozrast', 'rost_malch', 'otklon_rost_malch', 'ves_malch', 'otklon_ves_malch', 'rost_devoch', 'otklon_rost_devoch', 'ves_devoch', 'otklon_ves_devoch']

        widgets = {
            "vozrast": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "rost_malch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рост мальчика'
            }),
            "otklon_rost_malch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отклонение в росте мальчика'
            }),
            "ves_malch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес мальчика'
            }),
            "otklon_ves_malch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отклонение в весе мальчика'
            }),
            "rost_devoch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рост девочки'
            }),
            "otklon_rost_devoch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отклонение в росте девочки'
            }),
            "ves_devoch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес девочки'
            }),
            "otklon_ves_devoch": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отклоненипе в весе девочки'
            })
        }