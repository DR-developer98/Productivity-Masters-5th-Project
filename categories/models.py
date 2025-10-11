from django.db import models

class Category(models.Model):
    """
    Category model, will allow user
    to create their own categories for 
    to do tasks
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
