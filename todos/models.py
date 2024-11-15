from email.policy import default

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, help_text='Enter a title', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)
    description = models.TextField(help_text='Enter a description')