from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
# Create your models here.


class BasePage(Page):
    template = 'base_pages/home_page.html'

    body = RichTextField(max_length=1000)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
