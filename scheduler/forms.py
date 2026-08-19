from django import forms
from .models import StudySchedule


class StudyScheduleForm(forms.ModelForm):
    class Meta:
        model = StudySchedule
        fields = ['subject', 'topic', 'date', 'start_time', 'end_time', 'description', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
