from django.db import models

# Add these:
from wagtail.models import Page
from wagtail import blocks
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
# from wagtail.images.blocks import ImageBlock
from bakerydemo.base.blocks import ImageBlock


class TheBakerPage(Page):
    intro = RichTextField(blank=True)
    body2 = StreamField([
      ('heading', blocks.CharBlock(form_classname='title')),
      ('image', ImageBlock()),
      ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body2'),
    ]