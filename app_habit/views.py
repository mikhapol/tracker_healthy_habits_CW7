from rest_framework import generics

from app_habit.models import Habit
from app_habit.paginators import HabitPaginator
from app_habit.serializers import HabitSerializers


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializers


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек, но не более 5 на странице."""
    serializer_class = HabitSerializers
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр всех привычек."""
    serializer_class = HabitSerializers

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр привычки по ID"""
    serializer_class = HabitSerializers

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializers

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
