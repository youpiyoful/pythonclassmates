"""This models is common to all pages, it s an helper."""
from django.db import models
from taggit.models import TaggedItemBase, Tag as TaggitTag

from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet

@register_snippet
class Category(models.Model):
    """Category for all the website creation"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    class Meta: # noqa
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PageTag(TaggedItemBase):
    """Class of website tag"""
    content_object = ParentalKey('blog.PostPage', related_name='post_tags')

@register_snippet
class Tag(TaggitTag): # noqa
    class Meta: # noqa
        proxy = True