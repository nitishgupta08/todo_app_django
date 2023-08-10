"""
Models for the app
"""

from django.db import models
from django.utils import timezone
from django.conf import settings


class Tag(models.Model):
    """
    Tag Model Class
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return str(f"{self.name}")


class Todo(models.Model):
    """
    Todo Model Class
    """

    STATUS_CHOICES = (
        ("OPEN", "OPEN"),
        ("WORKING", "WORKING"),
        ("DONE", "DONE"),
        ("OVERDUE", "OVERDUE"),
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    high_priority = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(
        max_length=10,
        default="OPEN",
        choices=STATUS_CHOICES,
    )

    @property
    def is_overdue(self):
        """
        returns True if current date is greater than due date
        """
        return timezone.localdate() >= self.due_date

    def __str__(self) -> str:
        return str(f"{self.title}")
