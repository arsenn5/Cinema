from django.db import models
from django.contrib.auth.models import User

GENDER_TYPE = (
    ('Мужчина', 'Мужчина'),
    ('Женщина', 'Женщина')
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13,
                                    default='+996', verbose_name='Введите номер телефона')
    date_birth = models.DateField(verbose_name='Ваша дата рождения')
    gender = models.CharField(choices=GENDER_TYPE, max_length=20, verbose_name='Укажите пол')
