from rest_framework import serializers

from app_habit.models import Habit


class RelatedAndAwardValidator:
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """

    def __call__(self, value):
        related_habit = bool(dict(value).get("related_habit"))
        award = bool(dict(value).get("award"))

        if related_habit and award:
            raise serializers.ValidationError(
                "У привычки не может быть одновременно "
                "вознаграждения и связанной привычки")


class HabitTimeCompleteValidator:
    """
    Время выполнения должно быть не больше 120 секунд.
    """

    def __call__(self, value):
        time_complete = dict(value).get("time_complete")

        if isinstance(time_complete, int) and time_complete > 120:
            raise serializers.ValidationError(
                "Длительность привычки не может быть больше 120 секунд")


class HabitRelatedHabitIsPleasantValidator:
    """
    В связанные привычки могут попадать
    только привычки с признаком приятной привычки.
    """

    def __call__(self, value):
        related_habit = dict(value).get("related_habit")
        if related_habit:
            habit = Habit.objects.get(pk=related_habit.id)
            if not habit.is_pleasant:
                raise serializers.ValidationError(
                    "Связанная привычка должна быть приятной")


class HabitPleasantValidator:
    """
    У приятной привычки не может быть вознаграждения или связанной привычки.
    """

    def __call__(self, value):
        is_pleasant = dict(value).get("is_pleasant")
        award = bool(dict(value).get("award"))
        related_habit = bool(dict(value).get("related_habit"))

        if is_pleasant and award or is_pleasant and related_habit:
            raise serializers.ValidationError(
                "У приятной привычки не может быть "
                "вознаграждения или связанной привычки.")


class HabitFrequencyValidator:
    """
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    """

    def __call__(self, value):
        frequency = dict(value).get("frequency")
        if isinstance(frequency, int) and frequency > 7:
            raise serializers.ValidationError(
                "Привычка не должна выполняться реже чем раз в 7 дней")
