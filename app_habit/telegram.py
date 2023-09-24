import requests
from django.conf import settings

from users.models import User

URL = 'https://api.telegram.org/bot'
TOKEN = settings.TELEGRAM_TOKEN

def send_message(username, text):

    update = get_updates()
    if updates['ok']:
        parse_updates(update['result'])

    chat_id = User.objects.get(telegram=username).chat_id
    if not chat_id:
        print("Не возможно получить chat_id пользователя.")
        return

    data_for_request = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.get(
        url=f'{URL}{TOKEN}/sendMessage', data_for_request
    )
    return response.json()

def get_updates():
    response = requests.get(
        url=f'{URL}{TOKEN}/getUpdates'
    )
    return response.json()

def parse_updates(updates: dict):
    print(updates)
    for u in updates:
        user = User.objects.get(telegram=u['message']['chat']['username'])
        if User.objects.filter(telegram=user).exists():
            user.chat_id = u['message']['chat']['id']
            user.update_id = u['update_id']
            user.save()
