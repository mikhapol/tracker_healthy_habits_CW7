from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class User(AbstractUser):
    """Поля модели пользователя"""
    objects = UserManager()
    username = None

    telegram = models.CharField(max_length=20, verbose_name='ник в телеграме')
    email = models.EmailField(unique=True, verbose_name='почта')

    chat_id = models.IntegerField(verbose_name='ID чата', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
