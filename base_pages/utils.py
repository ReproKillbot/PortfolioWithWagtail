import re
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

context_menu = [
                'row_above',
                'row_below',
                '---------',
                'col_left',
                'col_right',
                '---------',
                'remove_row',
                'remove_col',
                '---------',
                'undo',
                'redo',
                '---------',
                'copy',
                'cut'
                '---------',
                'alignment',
            ]

small_table = {
            'startRows': 5,
            'startCols': 2,
            'contextMenu': context_menu
        }

large_table = {
    'startRows': 8,
    'startCols': 3,
    'contextMenu': context_menu
}

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# def build_menu_content(context, menu_items):
#     context['cartographers_menu'] = []
#     context['grimoire_menu'] = []
#     context['inspiration_menu'] = []
#     for item in menu_items:
#
#         if item.tags.filter(name__contains="Cartographer's Guide"):
#             context['cartographers_menu'].append(item)
#         if item.tags.filter(name__contains="Grey Grimoire"):
#             context['grimoire_menu'].append(item)
#         if item.tags.filter(name__contains="Font of Inspiration"):
#             context['inspiration_menu'].append(item)
#     return context


def search_by_tags(context, tags):
    """Split this stupid tag search string by comma, colons, or linebreaks"""
    tags = re.split('[,;|]', tags)
    tags_to_search = []
    """Start an empty list, add BlogPageTags if name is found in any search items - FINDING DUPLICATES"""
    for tag in tags:
        from base_pages.models import BlogPageTag
        blog_tag = BlogPageTag.objects.filter(name__contains=tag.capitalize())
        tags_to_search += blog_tag
    """Another stupid list, add id of the BLOG ITSELF """
    stupid_list = []
    for tag in tags_to_search:
        stupid_list.append(tag.content_object.id)
    all_posts = []
    """Clear this list of duplicate values (Since we've got the actual blog and not their tags, now)"""
    stupid_list = list(dict.fromkeys(stupid_list))
    for x in stupid_list:
        """Gimme all the actual blogs I need"""
        from base_pages.models import BlogPage
        all_posts.append(BlogPage.objects.get(pk=x))
    context["posts"] = all_posts
    return context


def paginate_posts(request, context, all_posts):
    paginator = Paginator(all_posts, 5)
    # Try to get the ?page=x value
    page = request.GET.get("page")
    try:
        # If the page exists and the ?page=x is an int
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the ?page=x is not an int; show the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the ?page=x is out of range (too high most likely) - Then return the last page
        posts = paginator.page(paginator.num_pages)

    # "posts" will have child pages; you'll need to use .specific in the template
    # in order to access child properties, such as youtube_video_id and subti
    context["posts"] = posts
    return context
