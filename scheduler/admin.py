from django.contrib import admin
from .models import StudySchedule


@admin.register(StudySchedule)
class StudyScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'topic',
        'date',
        'start_time',
        'end_time',
        'status',
        'user',
    )

    list_filter = ('status', 'date')
    search_fields = ('subject', 'topic', 'description')