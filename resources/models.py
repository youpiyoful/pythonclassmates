"""Page containing ResourcesPage and ResourcePage classes"""
from django.db import models
from wagtail.core.models import Page

class ResourcesPage(Page):
    """List all the resources of site"""
    subpage_types = [
        'ResourcePage',
    ]
    parent_page_types = []
    # title
    # description


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

    

