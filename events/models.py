"""The events page models."""
from django.db import models
from django import forms
from django.utils import timezone
# import datetime

from taggit.models import TaggedItemBase
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

from resources.models import ResourcePage, ResourcesPage


# class EventPageManager(PageManager):
#     """ Custom manager for Event pages """

# class EventPageQuerySet(PageQuerySet):
#     def future_start(self):
#         today = timezone.localtime(timezone.now()).date()
#         return self.filter(start__gte=today)
    
#     def future_end(self):
#         future_start = self.future_start()
#         return self.filter(end__gte=future_start)
    
# EventPageManager = PageManager.from_queryset(EventPageQuerySet)

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

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        event_page = EventPage.objects.live().public()
        print('event_page =====> ', event_page)
        context["events"] = event_page
        return context

    def send_data_to_resources_page(self):
        """
        copy the data found in the events table
        and the sends in the resource tables
        """
        # TODO
        today = timezone.localtime(timezone.now()).date()
        events_past = EventPage.objects.all().filter(end__lt=today)
        for event_past in events_past:
            try:
                ResourcePage.objects.get(title=event_past.title, description=event_past.description)
            except Page.DoesNotExist:
                resource_parent = ResourcesPage.objects.all()[0]
                resource = ResourcePage(title=event_past.title, slug=event_past.slug)
                resource_parent.add_child(instance=resource)
                # resource.publish()



    def delete_past_events(self):
        """Removes past events from the events table."""
        #TODO
        pass

    class Meta: #noqa
        verbose_name = "Events Page"
        verbose_name_plural = "Events Pages"

class EventPage(Page):
    """EventPage is the class of specific event"""
    subpage_types = []
    parent_page_types = ['EventsPage']

    body = RichTextField(blank=True)

    start = models.DateTimeField("start", null=True)
    end = models.DateTimeField('end', null=True)

    categories = ParentalManyToManyField('streams.Category', blank=True)
    tags = ClusterTaggableManager(through='events.EventPageTag', blank=True)

    # TODO
    # Empêcher que end soit antérieur à start à l'enregistrement d'une page
    # inscription
    # date


    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
        FieldPanel('start'),
        FieldPanel('end'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
        MultiFieldPanel(
            [
                InlinePanel("authors", label="Author", min_num=1, max_num=4)
            ],
            heading="Author(s)"
        ),
    ]

    class Meta: #noqa
        verbose_name = "Event Page"
        verbose_name_plural = "Event Pages"


class EventAuthorsOrderable(Orderable):
    """This allows us to select one or more event authors from Snippets."""

    page = ParentalKey("events.EventPage", related_name="authors")
    author = models.ForeignKey(
        "streams.Author",
        on_delete=models.CASCADE,
    )

    panels = [
    	# Use a SnippetChooserPanel because streams.Author is registered as a snippet
        SnippetChooserPanel("author"),
    ]

class EventPageTag(TaggedItemBase):
    """tag for events page"""
    content_object = ParentalKey('events.EventPage', related_name='event_tags')
