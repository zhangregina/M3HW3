from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser


class Custom_User(AbstractBaseUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    ADMIN = 1
    CLIENT = 2
    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (CLIENT, 'CLIENT'),
    )
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя', default=CLIENT)
    user_name = models.CharField('username', uqique=True, max_length=100),
    email = models.EmailField('email', null=True, max_length=100),
    first_name = models.CharField('first name', max_length=50, blank=True),
    last_name = models.CharField('last name', max_length=50, blank=True),
    date_joined = models.DateTimeField('date joined', auto_now_add=True),
    is_active = models.BooleanField('active', default=True),
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
