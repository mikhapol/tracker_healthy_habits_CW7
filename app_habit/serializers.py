from rest_framework import serializers

from app_habit.models import Habit
from app_habit.validators import RelatedAndAwardValidator, HabitTimeCompleteValidator, \
    HabitRelatedHabitIsPleasantValidator, HabitPleasantValidator, HabitFrequencyValidator


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedAndAwardValidator(),
            HabitTimeCompleteValidator(),
            HabitRelatedHabitIsPleasantValidator(),
            HabitPleasantValidator(),
            HabitFrequencyValidator(),
        ]
