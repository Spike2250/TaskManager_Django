from django.db import models
from django.utils.translation import gettext as _

from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(
        max_length=255, unique=True, blank=False,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description'),
    )
    author = models.ForeignKey(
        User, blank=False, on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        User, null=True, blank=True, default='', on_delete=models.PROTECT,
        related_name='executor',
        verbose_name=_('Executor'),
    )
    status = models.ForeignKey(
        Status, blank=False, on_delete=models.PROTECT,
        related_name='status',
        verbose_name=_('Status'),
    )
    labels = models.ManyToManyField(
        Label, blank=True,
        related_name='labels',
        verbose_name=_('Labels'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
