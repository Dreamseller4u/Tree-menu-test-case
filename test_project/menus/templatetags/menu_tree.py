from django import template
from django.template import RequestContext
from ..models import SubMenu

register = template.Library()


@register.inclusion_tag('menus/menus.html', takes_context=True)
def draw_menu(context: RequestContext, menu: str = '', parent: int = 0):

    if parent != 0:
        sub_items = context['sub_items']
        url_pk = context['url_pk']
    else:
        current_path_id = context['request'].path.replace('/', '')
        items = SubMenu.objects.select_related().filter(category__title=menu)
        tree_items = []
        sub_items = []

        if current_path_id:
            url_pk = int(current_path_id)
        else:
            url_pk = 0

        create_tree_by_url(items, url_pk, tree_items)

        for i in tree_items:
            sub_items.append({
                'id': i.id,
                'title': i.title,
                'parent': i.parent_id or 0,
                'child': i.children.all,
                'active': True if url_pk == i.id else False
            })
        sub_items = sorted(sub_items, key=lambda d: d['id'])
    return {
        'name': menu,
        'menu_items': [item for item in sub_items if 'parent' in item and item['parent'] == parent],
        'sub_items': sub_items,
        'url_pk': url_pk,
    }


def create_tree_by_url(lst: list, url_pk: int, re_lst: list):
    for i in lst:
        if i.id == url_pk and i not in re_lst:
            re_lst.append(i)
            for j in lst:
                if j.parent_id == i.parent_id and j not in re_lst:
                    re_lst.append(j)
            url_pk = i.parent_id
            create_tree_by_url(lst, url_pk, re_lst)
        else:
            if i.parent == None and i not in re_lst:
                re_lst.append(i)
