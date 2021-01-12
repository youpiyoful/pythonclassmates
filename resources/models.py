"""Page containing ResourcesPage and ResourcePage classes"""
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

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
    # description
    # link
    # title
    # publication_date
    # categories
    # tags
    # author

    
