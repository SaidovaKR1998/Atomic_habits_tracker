from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        # Дублируем валидацию из модели для работы через API
        if data.get('related_habit') and data.get('reward'):
            raise serializers.ValidationError("Нельзя указывать одновременно связанную привычку и вознаграждение.")
        if data.get('related_habit') and not data.get('related_habit').is_pleasant:
            raise serializers.ValidationError("В связанные привычки можно добавлять только приятные привычки.")
        if data.get('is_pleasant') and (data.get('reward') or data.get('related_habit')):
            raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
        if data.get('duration') and data['duration'] > 120:
            raise serializers.ValidationError("Время выполнения не может быть больше 120 секунд.")
        return data

