"""Integration tests of the resources app pages."""
from wagtail.images.blocks import ImageChooserBlock
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from blog.models import BlogPage, PostPage
from home.models import HomePage
from events.models import EventPage, EventsPage
from resources.models import ResourcesPage, ResourcePage
# from flex.models import FlexPage


class ResourcesPageTests(WagtailPageTests):
    """Resources page behavior test."""
    def test_can_create_only_resource_page(self):
        """test we can create only resourcePage from ResourcesPage"""
        self.assertCanNotCreateAt(ResourcesPage, HomePage)
        self.assertCanNotCreateAt(ResourcesPage, EventPage)
        self.assertCanNotCreateAt(ResourcesPage, EventsPage)
        self.assertCanNotCreateAt(ResourcesPage, BlogPage)
        # self.assertCanNotCreateAt(BlogPage, FlexPage)
        self.assertCanNotCreateAt(ResourcesPage, ResourcesPage)
        self.assertAllowedSubpageTypes(BlogPage, {PostPage})

    def test_can_create_resource_page(self):
        """
        We are testing that it's possible to create
        a resource page from the resources part.
        """
        self.assertCanCreateAt(ResourcesPage, ResourcePage)



class ResourcePageTests(WagtailPageTests):
    """Resource page behavior test."""
    def test_can_not_create_any_page(self):
        """
        we are testing that no child page 
        can be created from resourcePage.
        """
        self.assertCanNotCreateAt(ResourcePage, HomePage)
        self.assertCanNotCreateAt(ResourcePage, EventPage)
        self.assertCanNotCreateAt(ResourcePage, EventsPage)
        self.assertCanNotCreateAt(ResourcePage, BlogPage)
        self.assertCanNotCreateAt(ResourcePage, PostPage)
        # self.assertCanNotCreateAt(PostPage, FlexPage)
        self.assertCanNotCreateAt(ResourcePage, ResourcesPage)
        self.assertAllowedSubpageTypes(ResourcePage, {})
    
    def test_can_only_be_created_in_resources_page_parent(self):
        """
        Test that the resource page cannot be
        created in a parent other than the resourcespage.
        """
        self.assertAllowedParentPageTypes(
            ResourcePage, {ResourcesPage}
        )

    # def test_can_create_post_page(self):
    #     """ Test PostPageCreation are ok"""
    #     # Assert that a ContentPage can be made here, with this POST data
    #     self.assertCanCreate(BlogPage, PostPage, nested_form_data({
    #         'custom_title': 'About us',
    #         'content': streamfield([
    #             ('text', 'Lorem ipsum dolor sit amet'),
    #         ])
    #         # 'blog_image': ImageChooserBlock
    #     }))
        # custom_title
        # blog_image
        # description
        # content
        # categories
        # tags
        # content_panels