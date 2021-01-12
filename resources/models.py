"""Page containing ResourcesPage and ResourcePage classes"""
from django.db import models
from taggit.models import TaggedItemBase, Tag as TaggitTag
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from modelcluster.fields import ParentalKey, ParentalManyToManyField


class ResourcesPage(Page):
    """List all the resources of site"""
    subpage_types = [
        'ResourcePage',
    ]
    parent_page_types = ['home.HomePage']
    # title
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
    ]


    def get_context(self, request, *args, **kwargs):
        """Addind custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        resources = ResourcePage.objects.live().public()
        context["resources"] = resources
        return context

    class Meta: #noqa
        verbose_name = "Resources Page"
        verbose_name_plural = "Resources Pages"

class ResourcePage(Page):
    """Detail of specific resource"""
    subpage_types = []
    parent_page_types = ['ResourcesPage']
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='Overwrites the default title',
    )
    description = models.CharField(null=True, blank=False, max_length=255)
    # link
    # publication_date
    # categories
    # tags
    # author

    class Meta:
        verbose_name = "Resource Page"
        verbose_name_plural = "Resource pages"
