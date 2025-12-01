# habits/tasks.py
import requests
from celery import shared_task
from django.conf import settings


@shared_task
def send_telegram_reminder(habit_id):
    """
    Отправляет напоминание о привычке в Telegram
    """
    from .models import Habit

    try:
        habit = Habit.objects.get(id=habit_id)
        user = habit.user

        # Получаем chat_id из профиля пользователя
        if hasattr(user, 'profile') and user.profile.telegram_chat_id:
            chat_id = user.profile.telegram_chat_id

            message = f"🔔 Напоминание о привычке!\n\n" \
                      f"💫 Действие: {habit.action}\n" \
                      f"⏰ Время: {habit.time}\n" \
                      f"📍 Место: {habit.place}\n" \
                      f"⏱ Длительность: {habit.duration} секунд"

            url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
            data = {
                "chat_id": chat_id,
                "text": message,
                "parse_mode": "HTML"
            }

            response = requests.post(url, data=data)
            return f"Сообщение отправлено: {response.status_code}"
        else:
            return "У пользователя не указан Telegram Chat ID"

    except Habit.DoesNotExist:
        return "Привычка не найдена"
    except Exception as e:
        return f"Ошибка: {str(e)}"
