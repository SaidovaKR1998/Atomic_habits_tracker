# habits/services.py
from datetime import datetime, time, timedelta
from celery import shared_task
from .models import Habit
from .tasks import send_telegram_reminder


@shared_task
def check_and_send_habit_reminders():
    """
    Проверяет привычки, которые нужно выполнить в ближайшее время
    и отправляет напоминания
    """
    now = datetime.now().time()
    current_hour = now.hour
    current_minute = now.minute

    print(f"Проверка привычек в {now}")

    # Находим привычки, которые нужно выполнить в течение следующих 10 минут
    habits = Habit.objects.all()

    reminders_sent = 0

    for habit in habits:
        habit_time = habit.time

        # Проверяем, пора ли выполнять привычку
        time_diff = abs((habit_time.hour * 60 + habit_time.minute) -
                        (current_hour * 60 + current_minute))

        # Если время привычки в пределах 10 минут от текущего времени
        if time_diff <= 10:
            print(f"Напоминание для привычки: {habit.action} в {habit.time}")

            # Отправляем напоминание
            send_telegram_reminder.delay(habit.id)
            reminders_sent += 1

    return f"Отправлено {reminders_sent} напоминаний"
