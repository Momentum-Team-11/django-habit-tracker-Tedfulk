from habit.models import Habit, Result, User
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Habit
        fields = ('id', 'habit', 'goal', 'unit', 'user',)


class UserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = User
        fields = ('id', 'username')


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('id', 'daily_record', 'update_date', 'habit_record')