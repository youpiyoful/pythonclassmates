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

    description = models.CharField(max_length=255, blank=True,)
    # TODO card list

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        post_page = PostPage.objects.live().public()
        context["posts"] = post_page
        # time_from_last_update = now() - post_page.last_published_at
        # TODO faire un calcul pour déterminer depuis quand l'article à été créé.
        return context

    class Meta: #noqa
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"

# TODO : we can use get_context for list postpages in blog page instead of use
# get_children in the html template 
# https://www.youtube.com/watch?v=6YrbkE0_RPQ&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=16

class PostPage(Page):
    """PostPage is the page of specific articles"""
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
