from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a title", null=False, blank=False)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255, help_text="Enter a description")

    def clean(self):
        # Validação personalizada para garantir o formato de datas
        date_fields = ['deadline', 'finished_at']
        for field in date_fields:
            value = getattr(self, field)
            if value and not self.is_valid_date(value):
                raise ValidationError({field: f"{field} deve estar no formato YYYY-MM-DD."})

    @staticmethod
    def is_valid_date(value):
        try:
            datetime.strptime(str(value), '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def save(self, *args, **kwargs):
        self.deadline = self.ensure_iso_date(self.deadline)
        if self.finished_at:
            self.finished_at = self.ensure_iso_date(self.finished_at)
        super().save(*args, **kwargs)

    @staticmethod
    def ensure_iso_date(value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError(f"Data inválida: {value}. Deve estar no formato YYYY-MM-DD.")
        return value

    def __str__(self):
        return self.title
