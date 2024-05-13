from django.db import models

from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(
        max_length=255, unique=True, blank=False,
        verbose_name='Name',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
    )
    author = models.ForeignKey(
        User, blank=False, on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Author',
    )
    executor = models.ForeignKey(
        User, null=True, blank=True, default='', on_delete=models.PROTECT,
        related_name='executor',
        verbose_name='Executor',
    )
    status = models.ForeignKey(
        Status, blank=False, on_delete=models.PROTECT,
        related_name='status',
        verbose_name='Status',
    )
    labels = models.ManyToManyField(
        Label, blank=True,
        related_name='labels',
        verbose_name='Labels',
    )
    created_at = models.DateTimeField(auto_now_add=True)
