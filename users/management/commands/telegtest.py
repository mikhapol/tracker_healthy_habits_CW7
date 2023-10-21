from django.core.management import BaseCommand

from users.services import MyBot


class Command(BaseCommand):
    """
    Команда для тестовой отправки сообщения через телеграм бот.
    """

    def handle(self, *args, **options):
        my_bot = MyBot()
        my_bot.send_message('Проверка работоспособности телеграм бота.')
