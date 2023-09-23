from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""

        # Создание пользователя для тестирования
        self.user = User.objects.create(telegram='mikhapol',
                                        email='test@test.ru',
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True)

        self.user.set_password('qwerty')  # Устанавливаем пароль
        self.user.save()  # Сохраняем изменения пользователя в базе данных

        # Создание привычки для тестирования
        self.habit = Habit.objects.create(
            user=self.user,
            place="Парк",
            time="12:00",
            action="Глазеть на жопы",
            time_complete=20,
        )

        # Запрос токена для авторизации
        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': 'qwerty'})

        self.access_token = response.data.get('access')  # Токен для авторизации

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  # Авторизация пользователя

    def test_create_habit(self):
        """Тестирование создания привычки"""

        # Данные для создания привычки
        data = {
            "user": 1,
            "place": "Парк",
            "time": "12:00",
            "action": "Глазеть на жопы",
            "time_complete": 20
        }

        response = self.client.post(reverse('app_habit:habit_create'), data=data)  # Отправка запроса

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        self.assertEqual(Habit.objects.all().count(), 2)  # Проверка наличия в базе данных новой записи

    def test_public_list_habit(self):
        """Тестирование списка просмотра публичных привычек"""

        response = self.client.get(reverse('app_habit:habits_is_public'))  # Запрос на получение списка привычек

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(), [])

    def test_list_habit(self):
        """Тестирование списка просмотра личных привычек"""

        response = self.client.get(reverse('app_habit:habits'))  # Запрос на получение списка личных привычек

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json()['results'],
                         [{
                             "id": 1,
                             "place": "Парк",
                             "time": "12:00:00",
                             "action": "Глазеть на жопы",
                             "is_pleasant": False,
                             "frequency": 1,
                             "award": None,
                             "time_complete": 20,
                             "is_public": False,
                             "user": 1,
                             "related_habit": None
                         }])

    def test_update_habit(self):
        """Тестирование редактирования привычки"""

        # Данные для обновления привычки
        data = {
            "user": 1,
            "place": "Пляж",
            "time": "10:00",
            "action": "Глазеть на сиськи",
            "time_complete": 119
        }

        # Запрос на обновление урока
        response = self.client.put(reverse('app_habit:habit_update', args=[self.habit.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "id": 1,
                             "place": "Пляж",
                             "time": "10:00:00",
                             "action": "Глазеть на сиськи",
                             "is_pleasant": False,
                             "frequency": 1,
                             "award": None,
                             "time_complete": 119,
                             "is_public": False,
                             "user": 1,
                             "related_habit": None
                         })

    def test_get_habit_by_id(self):
        """Тестирование получения привычки по id"""

        # Запрос на получение привычки по id
        response = self.client.get(reverse('app_habit:habit', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "id": 1,
                             "place": "Парк",
                             "time": "12:00:00",
                             "action": "Глазеть на жопы",
                             "is_pleasant": False,
                             "frequency": 1,
                             "award": None,
                             "time_complete": 20,
                             "is_public": False,
                             "user": 1,
                             "related_habit": None
                         })

    def test_destroy_habit(self):
        """Тестирование удаления привычки"""

        # Запрос на удаление урока
        response = self.client.delete(reverse('app_habit:habit_delete', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

        self.assertEqual(Habit.objects.all().count(), 0)  # Проверка количества записей привычек в БД
