from datetime import datetime
from typing import List

from django.db import models


class BaseModel(models.Model):
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: bool = True


class Quote(BaseModel):
    STATUS_CHOICES: List[tuple] = [('New', 'New'), ('Moderated', 'Moderated')]

    text: str = models.TextField()
    author_name: str = models.CharField(max_length=150)
    author_email: str = models.EmailField()
    rating: int = models.IntegerField(default=0)
    status: str = models.CharField(choices=STATUS_CHOICES, default='New', max_length=100)

    def increment_rating(self) -> None:
        self.rating += 1
        self.save()

    def decrement_rating(self) -> None:
        self.rating -= 1
        self.save()

    class Meta:
        permissions: list = [
            ('view_not_moderated_quotes', 'can view not moderated quotes')
        ]

