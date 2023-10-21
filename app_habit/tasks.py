from datetime import datetime, timedelta

import requests
from celery import shared_task
from django.conf import settings

from app_habit.models import Habit
from app_habit.telegram import send_message
from users.models import User

URL = settings.TELEGRAM_URL_BOT
TOKEN = settings.TELEGRAM_TOKEN


@shared_task
def send_tg_message():
    """Отправка сообщения в телеграм"""
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=10)
    finish_time = time_now + timedelta(minutes=10)
    habits = Habit.objects.filter(time__gte=start_time).filter(time__lte=finish_time)

    for h in habits:
        action = h.action
        place = h.place
        time = h.time
        time_complete = h.time_complete
        user_tg = h.user.telegram

        updates = get_updates()
        if updates['ok']:
            parser_updates(updates['result'])

        chat_id = User.objects.get(telegram=user_tg).chat_id

        text = (f'Привычка {action} '
                f'в {place} '
                f'должна выполняться {time} '
                f'на протяжении {time_complete}')
        send_message(text, chat_id)

        h.time += timedelta(days=h.frequency)
        h.save()


def get_updates():
    """Получает CHAT_ID из ника telegram"""

    response = requests.get(f'{URL}{TOKEN}/getUpdates')
    # print(response.json())
    return response.json()


def parser_updates(updates):
    for u in updates:
        user = User.objects.get(telegram=u['message']['chat']['username'])
        if User.objects.filter(telegram=user).exist():
            user.chat_id = u['message']['chat']['id']
            user.update_id = u['update_id']
            user.save()
