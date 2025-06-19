# models.py

from django.db import models
from django.utils import timezone
from datetime import timedelta

class CreateTodo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isComplete = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)  # For trash timing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_expired(self):
        if self.isDeleted and self.deleted_at:
            return timezone.now() > self.deleted_at + timedelta(days=30)
        return False

    def __str__(self):
        return self.title
