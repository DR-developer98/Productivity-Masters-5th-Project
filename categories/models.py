from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category model, will allow user
    to create their own categories for 
    to do tasks
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('owner', 'name')

    def __str__(self):
        # ↓↓↓ CREDIT: Microsoft Copilot ↓↓↓
        return f"{self.name} ({self.owner.username})"
