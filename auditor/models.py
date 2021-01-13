"""Page about auditor class"""
from django.db import models


class Auditors(models.Model):
    """An auditor model."""

    email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')

    def __str__(self):
        """Str repr of this object."""
        return self.full_name

    class Meta:  # noqa
        verbose_name = "Auditor"
        verbose_name_plural = "Auditors"


