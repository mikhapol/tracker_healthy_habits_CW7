from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):
    """Поля модели привычек"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             **NULLABLE)
    place = models.CharField(max_length=150,
                             verbose_name='Место')
    time = models.DateTimeField(verbose_name='Время выполнения привычки')
    action = models.CharField(max_length=50,
                              verbose_name='Действие/Привычка')
    is_pleasant = models.BooleanField(default=False,
                                      verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('Habit',
                                      on_delete=models.SET_NULL,
                                      verbose_name='Связанная привычка',
                                      **NULLABLE)
    frequency = models.SmallIntegerField(default=1,
                                         verbose_name='Периодичность')
    award = models.CharField(max_length=50,
                             verbose_name='Вознаграждение',
                             **NULLABLE)
    time_complete = models.SmallIntegerField(
        verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False,
                                    verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('id',)
