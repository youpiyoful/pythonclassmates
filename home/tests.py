"""Integration tests of the home app pages."""
from flex.models import FlexPage
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from blog.models import BlogPage, PostPage
from home.models import HomePage
from events.models import EventPage, EventsPage
from resources.models import ResourcesPage, ResourcePage


class HomePageTests(WagtailPageTests):
    """Home page behavior test."""
    def test_home_page_allowed_events_blog_and_resources_page(self):
        """test homepage allowed only events, blog and resources page"""
        self.assertAllowedSubpageTypes(HomePage, {EventsPage, BlogPage, ResourcesPage, FlexPage})

    def test_can_create_blog_events_and_resources_page(self):
        """
        We are testing that it's possible to create
        a events, blog and resources page from the home part.
        """
        self.assertCanCreateAt(HomePage, BlogPage)
        self.assertCanCreateAt(HomePage, EventsPage)
        self.assertCanCreateAt(HomePage, ResourcesPage)

    def can_not_create_sub_sub_page(self):
        """
        verify we can not create subpage of subpage page in home page
        """
        self.assertCanNotCreateAt(HomePage, HomePage)
        self.assertCanNotCreateAt(HomePage, PostPage)
        self.assertCanNotCreateAt(HomePage, EventPage)
        self.assertCanNotCreateAt(HomePage, ResourcePage)
        # self.assertCanNotCreateAt(HomePage, FlexPage)

    def test_allowed_only_root_page_parent(self):
        """
        Test that the Home page allowed only root page parent
        """
        self.assertAllowedParentPageTypes(
            HomePage, {Page}
        )

    def test_home_page_can_be_created_in_root_page(self):
        """test than we can create an homepage only from root page parent"""
        self.assertCanCreateAt(Page, HomePage)