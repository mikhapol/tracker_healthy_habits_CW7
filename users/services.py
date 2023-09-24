import requests
from django.conf import settings


class MyBot:
    """
    Класс для отправки сообщения через бот телеграм.
    """
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN
    MY_ID = settings.TELEGRAM_USER_ID

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.MY_ID,
                'text': text
            }
        )
