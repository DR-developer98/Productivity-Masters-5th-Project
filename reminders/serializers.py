from rest_framework import serializers
from .models import Reminder
from tasks.models import Task


class ReminderSerializer(serializers.ModelSerializer):
    task_title = serializers.ReadOnlyField(source='task.title')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['task'].queryset = Task.objects.filter(
                owners=request.user)

    # ↓↓↓ CREDIT: Django documentations > Django utils ↓↓↓
    def validate_remind_at(self, value):
        from django.utils import timezone
        if value < timezone.now():
            raise serializers.ValidationError(
                "Remind time must be in the future.")
        return value
    # ↑↑↑ CREDIT: Django documentations > Django utils ↑↑↑ #

    class Meta:
        model = Reminder
        fields = [
            'id',
            'owner',
            'task',
            'task_title',
            'title',
            'note',
            'remind_at',
            'is_sent',
            'created_at',
            'updated_at',
            'is_owner',
        ]
        read_only_fields = ['owner']
