import requests
from django.conf import settings

URL = settings.TELEGRAM_URL_BOT
TOKEN = settings.TELEGRAM_TOKEN


def send_message(text, chat_id):
    requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': text
        }
    )
