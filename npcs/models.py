from django.contrib.admin.utils import quote
from django.db import models
from django.urls import reverse
from generic_chooser.widgets import AdminChooser
from modelcluster.fields import ParentalKey
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet



class NPC(Orderable):
    name = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=60)
    description = models.CharField(max_length=124)
    image = models.ImageField(null=True, blank=True)
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('sub_title'),
            FieldPanel('description'),
            ImageChooserPanel('image')
        ])
    ]

    def __str__(self):
        return f"{self.name} -- {self.sub_title}"


register_snippet(NPC)


class NPCChooser(AdminChooser):
    choose_one_text = _('Choose an NPC')
    choose_another_text = _('Choose another NPC')
    link_to_chosen_text = _('Edit this NPC')
    model = NPC
    choose_modal_url_name = 'npc_chooser:choose'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('npcs', 'npc', quote(item.pk)))


class NPCBlogRelationship(Orderable):
    blog = ParentalKey(
        'base_pages.BlogPage',
        related_name='npc_blog_relationship',
        on_delete=models.SET_NULL,
        null=True
    )
    npc = models.ForeignKey(
        NPC,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True
    )

    panels = [
        FieldPanel("npc", widget=NPCChooser),
    ]
