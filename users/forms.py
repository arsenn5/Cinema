from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

GENDER_TYPE = (
    ('Мужчина', 'Мужчина'),
    ('Женщина', 'Женщина')
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите ваш номер')
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_birth',
            'gender',
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
