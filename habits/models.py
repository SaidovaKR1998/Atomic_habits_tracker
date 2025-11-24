from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Habit(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=255, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='Связанная привычка')
    frequency = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='daily', verbose_name='Периодичность')
    reward = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вознаграждение')
    duration = models.PositiveIntegerField(help_text='Продолжительность в секундах', verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def clean(self):
        """
        Валидация на уровне модели (вызывается при вызове full_clean или при сохранении в админке).
        """
        # Исключить одновременный выбор связанной привычки и указания вознаграждения.
        if self.related_habit and self.reward:
            raise ValidationError("Нельзя указывать одновременно связанную привычку и вознаграждение.")

        # В связанные привычки могут попадать только привычки с признаком приятной привычки.
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("В связанные привычки можно добавлять только приятные привычки.")

        # У приятной привычки не может быть вознаграждения или связанной привычки.
        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")

        # Время выполнения должно быть не больше 120 секунд.
        if self.duration > 120:
            raise ValidationError("Время выполнения не может быть больше 120 секунд.")

    def save(self, *args, **kwargs):
        # Вызов полной валидации перед сохранением
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'