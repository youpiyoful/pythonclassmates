"""Streamfields live in here."""
# from typing import Text
from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta: # noqa
        # templates = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CTABlock(blocks.StructBlock):
    """A simple call to action section"""
    title = blocks.CharBlock(required=True,  max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_action = blocks.PageChooserBlock(required=False)
    # button_action_2 = blocks.PageChooserBlock(required=False)

    class Meta:
        icon = "placeholder"
        label = "Call to Action"