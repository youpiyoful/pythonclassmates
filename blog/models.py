"""Blog and post pages."""
from django.db import models
from django import forms

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

from streams import blocks


class BlogPage(Page):
    """Blog page class."""
    subpage_types = [
        'PostPage',
    ]

    parent_page_types = ['home.HomePage']

    # TODO trouver un moyen de bloquer l'édition de cette page !
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        post_page = PostPage.objects.live().public()
        context["posts"] = post_page
        return context

    class Meta: #noqa
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"

class PostPage(Page):
    """PostPage is the page of specific articles"""
    subpage_types = []
    parent_page_types = ['BlogPage']

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    description = models.CharField(null=False, blank=False, max_length=255)
    # table_of_recent_article
    # table_of_contents


    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    categories = ParentalManyToManyField('streams.Category', blank=True)
    tags = ClusterTaggableManager(through='streams.PageTag', blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        FieldPanel('description'),
        ImageChooserPanel('blog_image'),
        StreamFieldPanel('content'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

    class Meta: #noqa
        verbose_name = "Post Page"
        verbose_name_plural = "Post Pages"
