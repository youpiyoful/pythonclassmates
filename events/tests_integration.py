"""Integration tests of the blog app pages."""
from wagtail.images.blocks import ImageChooserBlock
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from events.models import EventPage, EventsPage
from home.models import HomePage
from blog.models import BlogPage, PostPage
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

    # def test_can_create_event_page(self):
    #     """ Test EventPage creation are ok"""
    #     events_page = EventsPage.objects.get(pk=8)
        # Assert that a ContentPage can be made here, with this POST data
        # self.assertCanCreate(events_page, EventPage, nested_form_data({
        #     'title': 'First Event',
        #     'body': streamfield([
        #         ('text', 'Lorem ipsum dolor sit amet'),
        #     ])
            # 'blog_image': ImageChooserBlock
        # }))
        # custom_title
        # blog_image
        # description
        # content
        # categories
        # tags
        # content_panels