from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from wagtail.core.models import Page

# from events.models import EventsPage
from events.models import EventPage
from resources.models import ResourcePage, ResourcesPage


class Command(BaseCommand):
    """
    launch methods send_data_to_resources and
    delete_past_events from EventsPage classes
    """
    help =  'launch methods send_data_to_resources anddelete_past_events from EventsPage classes'

    def handle(self, *args, **options):
        """copy event_past to resourcepage and delete event_past"""
        # send_events_past_to_resources = EventsPage.send_data_to_resources_page()
        # if send_events_past_to_resources:
        #     EventsPage.delete_past_events()
        today = timezone.localtime(timezone.now()).date()
        events_past = EventPage.objects.all().filter(end__lt=today)
        for event_past in events_past:
            try:
                ResourcePage.objects.get(title=event_past.title, slug=event_past.slug)
            except Page.DoesNotExist:
                resource_parent = ResourcesPage.objects.all()[0]
                resource = ResourcePage(title=event_past.title, slug=event_past.slug)
                resource_parent.add_child(instance=resource)
                event_past.delete()
                self.stdout.write(self.style.SUCCESS(
                    f'{event_past} is successfully copy in resourcePage and delete from EventPage ')
                )
        

