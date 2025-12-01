# habits/services.py
from datetime import datetime, time
from celery import shared_task
from .tasks import send_telegram_reminder


@shared_task
def check_and_send_habit_reminders():
    """
    Упрощенная версия для тестирования
    """
    now = datetime.now()
    print(f"⏰ Проверка привычек в {now.strftime('%H:%M:%S')}")

    # Просто отправляем тестовое сообщение
    result = test_task.delay()

    print(f"✅ Задача отправлена: {result.id}")
    return "Проверка завершена"
