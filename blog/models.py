"""The blog page models."""
from django.db import models
from django import forms
from modelcluster.models import ClusterableModel

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
# from streams.models import Category

class BlogPage(Page):
    """Blog page class."""

    description = models.CharField(max_length=255, blank=True,)
    # TODO card list 

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    class Meta: #noqa
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"

class PostPage(Page):
    """PostPage is the page of specific articles"""
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('streams.Category', blank=True)
    tags = ClusterTaggableManager(through='streams.PageTag', blank=True)
    # table_of_recent_article
    # table_of_contents

    content_panels = Page.content_panels + [
       FieldPanel('body', classname='full'), 
       FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
       FieldPanel('tags'),
    ]

    class Meta: #noqa
        verbose_name = "Post Page"
        verbose_name_plural = "Post Pages"

# @register_snippet
# class Category(models.Model):
#     """Category for all the website creation"""
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, max_length=80)

#     panels = [
#         FieldPanel('name'),
#         FieldPanel('slug'),
#     ]

#     class Meta: # noqa
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"