"""This models is common to all pages, it s an helper."""
from django.db import models
from taggit.models import TaggedItemBase, Tag as TaggitTag

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


@register_snippet
class Category(models.Model):
    """Category for all the website creation"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self): # noqa
        return self.name
    
    
    class Meta: # noqa
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PageTag(TaggedItemBase):
    """Class of website tag when u can add linked page with tags"""
    content_object = ParentalKey('blog.PostPage', related_name='post_tags')

@register_snippet
class Tag(TaggitTag): # noqa
    class Meta: # noqa
        proxy = True


@register_snippet
class Author(models.Model):
    """Author for snippets."""

    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    
    # image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=False,
    #     related_name="+",
    # )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                # Use an ImageChooserPanel because wagtailimages.Image (image property) 
                # is a ForeignKey to an Image
                # ImageChooserPanel("image"),
            ],
            heading="Name and Image",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading="Links"
        )
    ]

    def __str__(self):
        """String repr of this class."""
        return self.name

    class Meta:  # noqa
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"