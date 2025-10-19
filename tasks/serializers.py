from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from categories.models import Category


class TaskSerializer(serializers.ModelSerializer):
    # ↓↓↓ CREDIT: Microsoft Copilot + Django Rest Framework documentation ↓↓↓
    owners = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )
    # ↑↑↑ CREDIT: Microsoft Copilot + Django Rest Framework documentation ↑↑↑
    owner_usernames = serializers.SerializerMethodField()
    category_name = serializers.ReadOnlyField(source='category.name')
    is_overdue = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user in obj.owners.all()

    def get_owner_usernames(self, obj):
        return [user.username for user in obj.owners.all()]

    def get_is_overdue(self, obj):
        return obj.is_overdue()

    # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
    # Ensures each user can only see their own categories, 
    # when creating a task, instead of all categories in the 
    # database
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['category'].queryset = Category.objects.filter(owner=request.user)
    # ↑↑↑ CREDIT: Microsoft Copilot ↑↑↑

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'priority', 'state',
            'category', 'category_name', 'owners', 'created_at', 'updated_at', 
            'is_owner', 'is_overdue', 'owner_usernames',
        ]
