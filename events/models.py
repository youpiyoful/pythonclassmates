"""The events page models."""
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class EventsPage(Page):
    """Events page class."""

    subpage_types = [
        'EventPage',
    ]
    parent_page_types = []

    description = models.CharField(max_length=255, blank=True,)
    # TODO card list 

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    class Meta: #noqa
        verbose_name = "Events Page"
        verbose_name_plural = "Events Pages"

class EventPage(Page):
    """EventPage is the class of specific event"""
    subpage_types = []
    parent_page_types = ['EventsPage']

    body = RichTextField(blank=True)
    # TODO
    # inscription
    # date

    content_panels = Page.content_panels + [
       FieldPanel('body', classname='full'), 
    ]

    class Meta: #noqa
        verbose_name = "Event Page"
        verbose_name_plural = "Event Pages"