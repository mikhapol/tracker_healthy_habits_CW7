from django.urls import path
from app_habit.apps import AppHabitConfig
from app_habit.views import (HabitListAPIView, HabitCreateAPIView,
                             HabitRetrieveAPIView, HabitUpdateAPIView,
                             HabitDestroyAPIView, HabitPublicListAPIView)

app_name = AppHabitConfig.name

urlpatterns = [
    path('', HabitPublicListAPIView.as_view(), name='habits_is_public'),
    path('habits/', HabitListAPIView.as_view(), name='habits'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(),
         name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(),
         name='habit_delete'),
]
