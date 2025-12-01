# habits/services.py
from celery import shared_task


@shared_task(name='habits.services.check_and_send_habit_reminders')
def check_and_send_habit_reminders():
    """Проверка привычек"""
    print("✅ Проверка привычек запущена")
    return "Проверка завершена"
