from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import CustomUser


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        # Если вы используете email вместо username
        self.fields["username"].label = "Email"

        # Добавляем стили как в форме регистрации
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите ваш email"}
        )

        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text="Необязательное поле. Введите ваш номер телефона",
    )
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    username = forms.CharField(max_length=50, required=True)
    avatar = forms.ImageField(required=False, label="Аватар")
    country = CountryField().formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"}),
        required=False,
        label="Страна",
    )
    usable_password = None

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        fields_attrs = {
            "email": {"class": "form-control", "placeholder": "Введите почту"},
            "first_name": {"class": "form-control", "placeholder": "Введите имя"},
            "last_name": {"class": "form-control", "placeholder": "Введите фамилию"},
            "username": {"class": "form-control", "placeholder": "Введите ваш никнейм"},
            "phone_number": {"class": "form-control", "placeholder": "Номер телефона"},
            "avatar": {"class": "form-control-file"},
            "country": {"class": "form-control"},
            "password1": {"class": "form-control", "placeholder": "Введите пароль"},
            "password2": {"class": "form-control", "placeholder": "Повторите пароль"},
        }

        for field_name, attrs in fields_attrs.items():
            self.fields[field_name].widget.attrs.update(attrs)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "avatar",
            "country",
            "password1",
            "password2",
        )
        widgets = {"country": CountrySelectWidget()}

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")

        return phone_number
