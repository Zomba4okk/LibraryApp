from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.CharField(max_length=128)

    @property
    def is_available(self):
        return not self.logs.filter(returning_date__isnull=True).exists()

    @property
    def current_reader(self):
        return User.objects.filter(logs__book_id=self.id, logs__returning_date__isnull=True).first()

    def __str__(self):
        return f'{self.name} of {self.author}'


class BookLendingLog(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='logs')
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='logs')
    lending_date = models.DateField(default=datetime.now)
    returning_date = models.DateField(null=True, blank=True)

    @property
    def is_closed(self):
        return self.returning_date is not None
