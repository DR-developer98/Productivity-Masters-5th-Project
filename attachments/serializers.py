from rest_framework import serializers
from .models import Attachment
from tasks.models import Task

class AttachmentSerializer(serializers.ModelSerializer):
    task_title = serializers.ReadOnlyField(source='task.title')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user in obj.task.owners.all()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['task'].queryset = Task.objects.filter(owners=request.user)

    class Meta:
        model = Attachment
        fields = ['id', 'task', 'task_title', 'file', 'uploaded_at', 'is_owner']