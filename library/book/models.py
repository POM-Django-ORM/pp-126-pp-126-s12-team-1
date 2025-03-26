from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title})'
