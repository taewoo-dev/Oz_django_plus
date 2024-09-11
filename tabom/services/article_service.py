from django.core.paginator import Page, Paginator
from django.db.models import QuerySet

from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    return Article.objects.get(id=article_id)


def get_article_list(offset: int, limit: int) -> QuerySet[Article]:
    return Article.objects.order_by("-id").prefetch_related("like_set")[offset : offset + limit]


# def get_article_page(page: int, limit: int) -> Page[Article]:
#     return Paginator(Article.objects.order_by("-id"), limit).page(page)
