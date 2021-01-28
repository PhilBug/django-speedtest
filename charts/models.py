from django.db import models
from django.utils import timezone

class TestResult(models.Model):
    test_result = models.CharField(max_length=100)
    test_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
