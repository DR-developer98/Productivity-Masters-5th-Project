from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class Reminder(models.Model):
    """
    Reminder model for scheduling personal notifications linked to tasks.
    Each reminder belongs to a specific user and may optionally be associated
    with a task.
    Each task owner can create their individual reminder
    tailored to their own workflow

    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name='reminders')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='reminders')
    title = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    remind_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('task', 'owner', 'remind_at')

    def __str__(self):
        return f"Reminder for {self.owner.username} on \
            task '{self.task.title}'"
