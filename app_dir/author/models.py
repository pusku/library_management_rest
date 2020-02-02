from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now


class Author(models.Model):
    name = models.CharField(
        pgettext_lazy('Author field', 'name'),
        unique=True,
        max_length=128
    )
    created_at = models.DateTimeField(
        pgettext_lazy('Author field', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Author field', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'author'

    def __str__(self):
        return self.name
