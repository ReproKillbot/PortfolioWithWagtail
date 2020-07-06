from wagtail.core import hooks

from .views import QuestChooserViewSet


@hooks.register('register_admin_viewset')
def register_quest_chooser_viewset():
    return QuestChooserViewSet('quest_chooser', url_prefix='quest-chooser')
