from datetime import datetime
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a title", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, help_text="Enter a description")

    def deadline_as_date(self):
        return datetime.fromtimestamp(self.deadline).strftime('%d/%m/%Y %H:%M') if self.deadline else None

    def finished_as_date(self):
        return datetime.fromtimestamp(self.finished_at).strftime('%d/%m/%Y %H:%M') if self.finished_at else None
