
from django.db import models
from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet

from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from generic_chooser.widgets import AdminChooser
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.models import Orderable


QUEST_TYPES = (
    ('Escort', 'Escort'),
    ('Commission', 'Commission'),
    ('On The Road', 'On The Road'),
    ('Intrigue', 'Intrigue'),
    ('Rumor', 'Rumor'),
)


class Quest(Orderable):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=60, choices=QUEST_TYPES)
    description = models.CharField(max_length=124)

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('type'),
            FieldPanel('description'),
        ], heading="Quest Info", classname="collapsible")
    ]

    def __str__(self):
        return f"{self.name} -- {self.type}"


register_snippet(Quest)


class QuestChooser(AdminChooser):
    choose_one_text = _('Choose a Quest')
    choose_another_text = _('Choose another Quest')
    link_to_chosen_text = _('Edit this Quest')
    model = Quest
    choose_modal_url_name = 'quest_chooser:choose'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('quests', 'quest', quote(item.pk)))


class QuestBlogRelationship(Orderable):
    blog = ParentalKey(
        'base_pages.BlogPage',
        related_name='quest_blog_relationship',
        on_delete=models.SET_NULL,
        null=True
    )
    quest = models.ForeignKey(
        Quest,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True
    )

    panels = [
        FieldPanel("quest", widget=QuestChooser),
    ]
