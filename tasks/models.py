from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from django.utils import timezone


class Task(models.Model):
    """
    Task model for 
    """
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    STATE_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In progress'),
        ('done', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length = 255, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='open')
    # ↓↓↓ CREDIT: Stackoverflow (on_delete=models.SET_NULL) ↓↓↓
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # ↑↑↑ CREDIT: Stackoverflow (on_delete=models.SET_NULL) ↑↑↑
    owners = models.ManyToManyField(User, related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_overdue(self):
        # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
        return self.due_date and self.due_date < timezone.now() and self.state != 'done'

    def __str__(self):
        # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
        return f"{self.title} ({', '.join([user.username for user in self.owners.all()])})"
