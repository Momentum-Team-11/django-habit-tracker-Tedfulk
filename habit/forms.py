from django import forms
from .models import Habit, Result


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'habit',
            'goal',
            'unit',
        ]


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            'daily_record',
            'update_date',
            'completed',
            
        ]
