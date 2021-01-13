"""Integration tests of the blog app pages."""
# from wagtail.images.blocks import ImageChooserBlock
from unittest.case import SkipTest
from resources.models import ResourcesPage
from wagtail.core.models import Page
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from events.models import EventPage, EventsPage
from home.models import HomePage
from blog.models import BlogPage, PostPage
from events.management.commands.copy_and_delete_past_event import Command
from django.utils import timezone
# from flex.models import FlexPage
# from resources import ResourcesPage


class EventsPageTests(WagtailPageTests):
    """Events page behavior test."""
    def test_can_create_only_event_page(self):
        """test we can create only eventPage from EventsPage"""
        self.assertCanNotCreateAt(EventsPage, HomePage)
        self.assertCanNotCreateAt(EventsPage, PostPage)
        self.assertCanNotCreateAt(EventsPage, EventsPage)
        self.assertCanNotCreateAt(EventsPage, BlogPage)
        # self.assertCanNotCreateAt(EventsPage, FlexPage)
        # self.assertCanNotCreateAt(EventsPage, ResourcesPage
        self.assertAllowedSubpageTypes(EventsPage, {EventPage})

    def test_can_create_event_page(self):
        """
        We are testing that it's possible to create
        an event page from the blog part.
        """
        self.assertCanCreateAt(EventsPage, EventPage)



class EventPageTests(WagtailPageTests):
    """Event page behavior test."""
    # fixtures = ['data.json']
    # @classmethod
    # def setUpTestData(cls):
    #     """Init the db for the tests of class"""
    #     events_page = EventsPage.objects.create(
    #         page_ptr_id=1,
    #         description="page des évènements",
    #         path="000001111222",
    #         depth=3,
    #         title="page d'évènements",
    #         slug="events-page",
    #     )
    #     print("id events_page =======> ", events_page.id)


    def test_can_not_create_any_page(self):
        """
        we are testing that no child page 
        can be created from EventPage.
        """
        self.assertCanNotCreateAt(EventPage, HomePage)
        self.assertCanNotCreateAt(EventPage, EventPage)
        self.assertCanNotCreateAt(EventPage, EventsPage)
        self.assertCanNotCreateAt(EventPage, BlogPage)
        self.assertCanNotCreateAt(EventPage, PostPage)
        # self.assertCanNotCreateAt(EventPage, FlexPage)
        # self.assertCanNotCreateAt(EventPage, ResourcesPage)
        self.assertAllowedSubpageTypes(EventPage, {})
    
    def test_can_only_be_created_in_events_page_parent(self):
        """
        Test that the event page cannot be
        created in a parent other than the EventsPage.
        """
        self.assertAllowedParentPageTypes(
            EventPage, {EventsPage}
        )

    # def setUp(self):
    #     EventsPage.objects.create(
    #         description="page des évènements",
    #         path="000001111222",
    #         depth=3,
    #         title="page d'évènements",
    #         slug="events-page",
    #     )
    # def setUp(self):
    #     # Test definitions as before.
    #     call_setup_methods()

    # def test_can_create_event_page(self):
    #     """ Test EventPage creation are ok"""
    #     events_page = EventsPage.objects.all()[0]
    #     # events_page = cls.events_page
    #     # Assert that a ContentPage can be made here, with this POST data
    #     self.assertCanCreate(events_page, EventPage, nested_form_data({
    #         'title': 'First Event',
    #         'body': streamfield([
    #             ('text', 'Lorem ipsum dolor sit amet'),
    #         ])
    # }))
        # custom_title
        # blog_image
        # description
        # content
        # categories
        # tags
        # content_panels

@SkipTest
class CommandTest(WagtailPageTests):
    """
    Test the custom django command which copies past
    events to resources before deleting them.
    """
    fixtures = ['data.json']

    def test_event_past_is_successfully_copy_and_delete(self):
        """ Test than event past is copy to resources and delete from events"""
        
        # self.assertIsNone(self.events_past)
        today = timezone.localtime(timezone.now()).date()
        event_past = EventsPage.objects.all().filter(end_lt=today)
        
        # control than event_past exist and he is less than today
        self.assertLess(event_past, today)
        resources = ResourcesPage.objects.all()

        # control than resources is empty
        self.assertEqual(len(resources), 0)
        Command.handle()

        # check than resources is created
        self.assertEqual(len(resources), 1)
        
        # control than event_past len() is equal to 0 after custom cmd copy and delete
        self.assertEquals(len(event_past), 0)


    def test_than_resources_is_child_of_resource(self):
        """check than resources exist in the child_of resource page"""
        resource_parent = ResourcesPage.get_children().live()
        
        # check than resource_parent have no children before cmd.hanle()
        self.assertEqual(len(resource_parent), 0)
        Command.handle()
        
        # check than resource_parent have one children or more
        self.assertTrue(len(resource_parent) >= 1)