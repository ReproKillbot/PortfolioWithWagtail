from django.utils.translation import ugettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from .models import NPC


class NPCChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = NPC
    page_title = _("Choose a NPC")
    per_page = 10
    order_by = 'name'
    fields = [
        'name',
        'sub_title',
        'description',
        'image',
    ]
