from django.db import models
from tasks.models import Task


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name='attachments')
    file = models.FileField(upload_to='task_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.task.title}"
