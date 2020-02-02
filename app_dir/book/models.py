from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now
from app_dir.author.models import Author

class Book(models.Model):
    title = models.CharField(
        pgettext_lazy('Book field', 'name'),
        unique=True,
        max_length=128
    )

    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        pgettext_lazy('Book field', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Book field', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'book'

    def __str__(self):
        return self.title
