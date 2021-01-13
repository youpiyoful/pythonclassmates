"""Home page models."""
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from streams import blocks


class HomePage(Page):
    """Home page model."""

    # templates = ""
    # max_count = 3
    parent_page_types = ['wagtailcore.Page']
    subpage_types = [
        'blog.BlogPage',
        'events.EventsPage',
        'resources.ResourcesPage',
        'flex.FlexPage',
    ]
    banner_title = models.CharField(max_length=100, blank=False, null=True,)
    banner_subtitle = RichTextField(features=['bold', 'italic'])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    banner_cta = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content = StreamField(
        [
            ("cta", blocks.CTABlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta'),
        StreamFieldPanel("content"),
    ]

    class Meta: # noqa
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
