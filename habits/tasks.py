import requests
from celery import shared_task
from django.conf import settings
from .models import Habit

@shared_task
def send_telegram_reminder(habit_id):
    habit = Habit.objects.get(id=habit_id)
    # Предполагается, что у модели User есть поле telegram_chat_id
    chat_id = habit.user.telegram_chat_id

    if chat_id:
        message = f"Напоминание: Пора {habit.action} в {habit.time} в {habit.place}!"
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }
        requests.post(url, data=data)
