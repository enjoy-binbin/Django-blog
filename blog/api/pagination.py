from rest_framework.pagination import (
    LimitOffsetPagination,  # 分页器 ?limit=2&offset=1
    PageNumberPagination,  # 分页器 ?page=1
)


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2  # 默认一页两条
    max_limit = 10  # 最多一页十条


class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 2  # 一页两条
