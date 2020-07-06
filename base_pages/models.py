from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock

from base_pages.utils import remove_html_tags, search_by_tags, paginate_posts, small_table, large_table


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'base_pages.BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name is "":
            self.name = str(self.tag)
        super().save(force_insert, force_update, using, update_fields)


class BasePage(Page):
    body = RichTextField(max_length=5000)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class BlogListingPage(RoutablePageMixin, Page):
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')
        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            context = search_by_tags(context, tags)
            context["tags"] = tags
            return context
        context = paginate_posts(request, context, all_posts)
        return context


class BlogPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('small_table', TableBlock(table_options=small_table)),
        ('large_table', TableBlock(table_options=large_table)),
    ])
    thumbnail = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    @property
    def intro(self):
        intro_text = ''
        blocks = self.body.stream_data
        for block in blocks:
            if block['type'] == "paragraph":
                intro_text = "&emsp;&emsp;&emsp;" + remove_html_tags(block['value'][:300]) + "..."
                break
        return intro_text

    @property
    def npcs(self):
        npcs = [
            n.npc for n in self.npc_blog_relationship.all()
        ]
        return npcs

    @property
    def quests(self):
        quests = [
            q.quest for q in self.quest_blog_relationship.all()
        ]
        return quests

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('thumbnail'),
                ], heading="Thumbnail", classname="collapsible collapsed"),
        MultiFieldPanel([
            InlinePanel('npc_blog_relationship'),
            InlinePanel('quest_blog_relationship'),
        ],
            heading="Blog Extras -- NPC's and Quests",
            classname="collapsible collapsed"),
        FieldPanel('tags', heading="Tags")
    ]

    def save(self, *args, **kwargs):
        if self.id is None:
            self.show_in_menus = True
            self.show_in_menus_default = True
        return super().save()
