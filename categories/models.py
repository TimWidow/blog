"""Categories"""

from django.db import models


# Models

# Create your models here.
class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
