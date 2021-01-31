from django.db import models
from django.utils import timezone

class TestResult(models.Model):
    result = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=100, default='unknown')

    def __str__(self):
        return str(self.id)
