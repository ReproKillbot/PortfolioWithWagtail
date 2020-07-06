from django.utils.translation import ugettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from .models import Quest


class QuestChooserViewSet(ModelChooserViewSet):
    icon = 'user'
    model = Quest
    page_title = _("Choose a Quest")
    per_page = 10
    order_by = 'name'
    fields = [
        'name',
        'type',
        'description'
    ]
