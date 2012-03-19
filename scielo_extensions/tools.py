from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from django.conf import settings


def get_paginated(items, page_num, items_per_page=settings.PAGINATION__ITEMS_PER_PAGE):
    """
    Wraps django core pagination object
    """
    paginator = Paginator(items, items_per_page)

    try:
        page_num = int(page_num)
    except ValueError:
        raise TypeError('page_num must be integer')

    try:
      paginated = paginator.page(page_num)
    except EmptyPage:
      paginated = paginator.page(paginator.num_pages)

    return paginated