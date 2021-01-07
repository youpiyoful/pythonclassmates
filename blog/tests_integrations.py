"""Integration tests of the blog app pages."""
from wagtail.images.blocks import ImageChooserBlock
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield
from blog.models import BlogPage, PostPage
from home.models import HomePage
from events.models import EventPage, EventsPage
# from flex.models import FlexPage
# from resources import ResourcesPage


class BlogPageTests(WagtailPageTests):
    """Blog page behavior test."""
    def test_can_create_only_post_page(self):
        """test we can create only postPage from blogPage"""
        self.assertCanNotCreateAt(BlogPage, HomePage)
        self.assertCanNotCreateAt(BlogPage, EventPage)
        self.assertCanNotCreateAt(BlogPage, EventsPage)
        self.assertCanNotCreateAt(BlogPage, BlogPage)
        # self.assertCanNotCreateAt(BlogPage, FlexPage)
        # self.assertCanNotCreateAt(BlogPage, ResourcesPage
        self.assertAllowedSubpageTypes(BlogPage, {PostPage})

    def test_can_create_post_page(self):
        """
        We are testing that it's possible to create
        a post page from the blog part.
        """
        self.assertCanCreateAt(BlogPage, PostPage)



class PostPageTests(WagtailPageTests):
    """Post page behavior test."""
    def test_can_not_create_any_page(self):
        """
        we are testing that no child page 
        can be created from postPage.
        """
        self.assertCanNotCreateAt(PostPage, HomePage)
        self.assertCanNotCreateAt(PostPage, EventPage)
        self.assertCanNotCreateAt(PostPage, EventsPage)
        self.assertCanNotCreateAt(PostPage, BlogPage)
        self.assertCanNotCreateAt(PostPage, PostPage)
        # self.assertCanNotCreateAt(PostPage, FlexPage)
        # self.assertCanNotCreateAt(PostPage, ResourcesPage)
        self.assertAllowedSubpageTypes(PostPage, {})
    
    def test_can_only_be_created_in_blog_page_parent(self):
        """
        Test that the post page cannot be
        created in a parent other than the blogpage.
        """
        self.assertAllowedParentPageTypes(
            PostPage, {BlogPage}
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