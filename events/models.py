"""The events page models."""
from auditor.models import Auditors
from django.db import models
from django import forms
from django.utils import timezone
from django.shortcuts import redirect, render

# import datetime

from taggit.models import TaggedItemBase
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

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
    parent_page_types = [
        'home.HomePage'
    ]

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

    @staticmethod
    def send_data_to_resources_page():
        """
        copy the data found in the events table
        and the sends in the resource tables
        """
        # TODO créer une crontask pour lancer la fonction une fois par jour
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


    @staticmethod
    def delete_past_events():
        """Removes past events from the events table."""
        #TODO create a django custom cmd with this method
        today = timezone.localtime(timezone.now()).date()
        events_past = EventPage.objects.all().filter(end__lt=today)
        for event_past in events_past:
            event_past.delete()
        

    class Meta: #noqa
        verbose_name = "Events Page"
        verbose_name_plural = "Events Pages"

class EventPage(RoutablePageMixin, Page):
    """EventPage is the class of specific event"""
    subpage_types = []
    parent_page_types = ['EventsPage']

    body = RichTextField(blank=True)
    start = models.DateTimeField("start", null=True)
    end = models.DateTimeField('end', null=True)
    categories = ParentalManyToManyField('streams.Category', blank=True)
    tags = ClusterTaggableManager(through='events.EventPageTag', blank=True)
    auditors = models.ManyToManyField(Auditors)

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
        # InlinePanel("authors", label="Author", max_num=1),
        MultiFieldPanel(
            [
                InlinePanel("authors", label="Author", max_num=1) # min_num=1, max_num=4
            ],
            heading="Author"
        ),
    ]

    class Meta: #noqa
        verbose_name = "Event Page"
        verbose_name_plural = "Event Pages"

    @route(r'^event-register/$')
    def event_register(self, request, *args, **kwargs):
        event_id = request.POST.get('eventId')
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        print('data => ', event_id, full_name, email)
        # context = self.get_context(request, *args, **kwargs)
        # return render(request, "home/subscribe.html", context)
        event_page = EventsPage.objects.all()[0]
        return redirect('http://localhost:8000/events/')


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
